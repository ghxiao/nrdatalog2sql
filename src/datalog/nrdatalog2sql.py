"""Convert Non-Recursive Datalog programs to SQL queries."""

import sys
import os
from collections import defaultdict
from functools import reduce
import itertools

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import networkx as nx

from datalog.model import Variable, Term, NafLiteral, Rule, Program
import datalog.yacc

# Vocabulary type: { predicate_name -> (encode, type_) }
Vocab = dict[str, tuple[int, int]]


def main(argv: list[str]) -> None:
    """Parse a Datalog program and print the equivalent SQL query."""
    vocab = read_tbox_name(argv[2])

    parser = datalog.yacc.parser
    datalog_string = open(argv[1]).read()
    program: Program = parser.parse(datalog_string)

    G = nx.DiGraph()
    for rule in program.rules:
        for body_literal in rule.body:
            G.add_edge(body_literal.predicate, rule.head.predicate)

    depends = list(nx.topological_sort(G))

    sql = "WITH \n %s ,\n" % ",\n".join(
        [edb2sfw(p, *vocab[p]) for p in (set(depends) & set(vocab.keys()))]
    )

    ctes = [
        rules2cte(rules)
        for rules in (
            [r for r in program.rules if r.head.predicate == p]
            for p in depends
        )
        if rules
    ]

    sql += ",\n".join(ctes)

    last = reduce(lambda x, y: y, depends)
    sql += "\n SELECT COUNT(*) FROM %s" % last

    print(sql)


def rules2cte(rules: list[Rule]) -> str:
    """Convert rules sharing a common head predicate to a SQL CTE."""
    union = " UNION\n ".join(rule2sfw(rule) for rule in rules)
    return "%s AS (%s)" % (rules[0].head.predicate, union)


def rule2sfw(rule: Rule) -> str:
    """Convert a single Datalog rule to a SQL SELECT-FROM-WHERE block."""
    # Map each variable to all (literal, term_index, literal_index) occurrences
    var2literals: dict[Term, list[tuple[NafLiteral, int, int]]] = defaultdict(list)
    for k, lit in enumerate(rule.body):
        for i, t in enumerate(lit.terms):
            var2literals[t].append((lit, i, k))

    vars_ = [
        "atom_%d.att_%d " % (rule.body.index(var2literals[term][0][0]), var2literals[term][0][1])
        for term in rule.head.terms
    ]
    vars_ = ["%s AS att_%d" % (v, i) for i, v in enumerate(vars_)]

    s = "\n SELECT DISTINCT %s " % ", ".join(vars_)

    f = "\n FROM\n%s" % ",\n".join(
        "%s AS atom_%d" % (literal.predicate, index)
        for index, literal in enumerate(rule.body)
    )

    conds = list(
        itertools.chain(
            *[
                [
                    "atom_%d.att_%d = atom_%d.att_%d"
                    % (lst[0][2], lst[0][1], lst[k][2], lst[k][1])
                    for k in range(1, len(lst))
                ]
                for lst in var2literals.values()
            ]
        )
    )

    w = ("\n WHERE " + " AND ".join(conds)) if conds else ""

    return "(%s %s %s)" % (s, f, w)


def edb2sfw(predicate: str, encode: int, type_: int) -> str:
    """Convert an EDB predicate to a SQL CTE based on its OWLGres type.

    Types (as defined in OWLGres):
      1 - concept assertion
      2 - object property
      3 - data property
    """
    if type_ == 1:
        return (
            "%s AS ( \n"
            "  SELECT ca.individual AS att_0 \n"
            "  FROM concept_assertion AS ca \n"
            "  WHERE concept = %d \n"
            ")"
        ) % (predicate, encode)
    elif type_ == 2:
        return (
            "%s AS ( \n"
            "  SELECT ora.a AS att_0, ora.b AS att_1 \n"
            "  FROM object_role_assertion AS ora \n"
            "  WHERE object_role = %d \n"
            ")"
        ) % (predicate, encode)
    elif type_ == 3:
        return (
            "%s AS ( \n"
            "  SELECT dra.a AS att_0, dra.b AS att_1 \n"
            "  FROM data_role_assertion AS dra \n"
            "  WHERE data_role = %d \n"
            ")"
        ) % (predicate, encode)
    else:
        raise ValueError("Unsupported OWLGres type: %d" % type_)


def read_tbox_name(fname: str) -> Vocab:
    """Read a TBox name file and return a vocabulary mapping.

    The file format is the output of ``SELECT * FROM tbox_name`` in PostgreSQL.
    Returns a dict mapping fragment names to (encode, type) pairs.
    """
    with open(fname) as f:
        f.readline()
        f.readline()
        return {
            frag(sp[4].strip()): (int(sp[0].strip()), int(sp[1].strip()))
            for sp in (line.strip().split("|") for line in f)
            if len(sp) == 5 and "#" in sp[4]
        }


def frag(url: str) -> str:
    """Extract the fragment (local name) from a URL after '#'."""
    return url[url.rindex("#") + 1:]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python nrdatalog2sql.py datalog.dl vocab.txt")
        sys.exit(-1)
    main(sys.argv)

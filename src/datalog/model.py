"""Data model for Non-Recursive Datalog programs."""

from __future__ import annotations


class Term:
    """Base class for Datalog terms."""

    name: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Term):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class Variable(Term):
    """A Datalog variable (uppercase identifier)."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Variable({self.name!r})"


class Constant(Term):
    """A Datalog constant (symbolic or string literal)."""

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Constant({self.name!r})"


class NafLiteral:
    """A (possibly negated) Datalog literal."""

    def __init__(
        self,
        predicate: str,
        terms: list[Term],
        neg: bool = False,
        naf: bool = False,
    ) -> None:
        self.predicate = predicate
        self.terms = terms
        self.neg = neg
        self.naf = naf

    def __str__(self) -> str:
        prefix = ("not " if self.naf else "") + ("-" if self.neg else "")
        args = ", ".join(str(t) for t in self.terms)
        return f"{prefix}{self.predicate}({args})"

    def __repr__(self) -> str:
        return (
            f"NafLiteral({self.predicate!r}, {self.terms!r},"
            f" neg={self.neg}, naf={self.naf})"
        )


class Rule:
    """A Datalog rule of the form: head :- body."""

    def __init__(self, head: NafLiteral, body: list[NafLiteral]) -> None:
        self.head = head
        self.body = body

    def __str__(self) -> str:
        return f"{self.head} :- {', '.join(str(lit) for lit in self.body)}."

    def __repr__(self) -> str:
        return f"Rule({self.head!r}, {self.body!r})"


class Program:
    """A Datalog program: an ordered list of rules."""

    def __init__(self, rules: list[Rule]) -> None:
        self.rules = rules

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.rules)

    def __repr__(self) -> str:
        return f"Program({self.rules!r})"

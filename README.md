# Non-Recursive Datalog to SQL Converter

This python project is a converter from Non-Recursive Datalog to SQL Query, which can be
executed directly on PostgreSQL/OWLGres.

## Dependencies

- [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/)
  Datalog Parser
- [NetworkX](http://networkx.github.com/)
  Dependency Analysis
  
These dependencies can be installed by [PIP](http://www.pip-installer.org/) from [PyPI](http://pypi.python.org/pypi)

## Usage

We assume that the OWL 2 QL ontology is loaded into PostgreSQL by OWLGres.

```console
$ ./src/datalog/datalog2sql.py datalog.dl tbox_name.txt > query.sql
```
- datalog.dl is a non-recursive Datalog program with DL predicates
  from the OWL 2 QL ontology
- tbox_name.txt is the output of query `SELECT * FROM tbox_name` FROM PostgreSQL/OWLGres.


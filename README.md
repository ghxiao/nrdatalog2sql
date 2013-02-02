# Non-Recursive Datalog to Datalog Converter

This python project is a converter to Non-Recursive Datalog to SQL Query, which can be
executed directly on PostgreSQL/OWLGres.

## Dependency

- [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/)
  Datalog Parser
- [NetworkX](http://networkx.github.com/)
  Dependency Analysis
  
These dependencies can be installed by [PIP](http://www.pip-installer.org/) from [PyPI](http://pypi.python.org/pypi)

## Usage

We assume that the data is loaded by OWLGres into Postgres.

```console
$ ./src/datalog/datalog2sql.py datalog.dl tbox_name.txt > query.sql
```
- datalog.dl is a non-recursive Datalog program
- tbox_name.txt is the output of query `SELECT * FROM tbox_name` FROM PostgreSQL/OWLGres.


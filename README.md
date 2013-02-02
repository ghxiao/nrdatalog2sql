# Non-Recursive Datalog to Datalog Converter

This project converts Non-Recursive Datalog to SQL Query, which can be
executed directly on PostgreSQL.

## Dependency

- PLY (Python Lex-Yacc)
  For Datalog Parser
- Networkx
  Dependency Analysis
  
These dependencies can be installed by PIP from PyPI

## Usage

We assume that the data is loaded by OWLGres into Postgres.

```console
./datalog2sql.py datalog.dl tbox_name.txt > query.sql
```
- datalog.dl is a non-recursive Datalog program
- tbox_name.txt is the output of query `SELECT * FROM tbox_name` FROM OWLGres.


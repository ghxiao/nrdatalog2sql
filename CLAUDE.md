# CLAUDE.md

## Project Overview

**nrdatalog2sql** is a Python tool that converts Non-Recursive Datalog programs to SQL queries executable on PostgreSQL/OWLGres.

## Key Files

- `src/datalog/nrdatalog2sql.py` — main entry point / CLI
- `src/datalog/lex.py` — Datalog lexer (PLY)
- `src/datalog/yacc.py` — Datalog parser (PLY)
- `src/datalog/model.py` — Datalog data model
- `data/q1.dl` — example Datalog program
- `data/LUBM-ex-20_tbox-name.txt` — example TBox name file

## Usage

```bash
./src/datalog/nrdatalog2sql.py <datalog.dl> <tbox_name.txt> > query.sql
```

## Dependencies

- Python 3
- [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/) — parsing
- [NetworkX](http://networkx.github.com/) — dependency analysis

Install via pip:
```bash
pip install ply networkx
```

## Notes

- Only non-recursive Datalog programs are supported
- Designed to work with OWL 2 QL ontologies loaded via OWLGres into PostgreSQL

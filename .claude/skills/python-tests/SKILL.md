---
name: python-tests
description: Pytest conventions for this repo. Use whenever writing, fixing, or judging tests in src/tests/.
---
## Layout
- `src/<folder>/<file>.py` maps to `src/tests/<folder>_<file>_test.py`, one test file per module.
- Skip `__init__.py`, `src/tests/`, `src/data/`, and `src/outputs/`.
- Run with `.venv/bin/python -m pytest -q src/tests`.

## Writing tests
- Name tests `test_<function>_<behaviour>` (e.g. `test_idf_term_in_every_doc_is_zero`).
- Use small, hand-computed inputs and outputs, and `pytest.approx` for floats.
- Use `pytest.mark.parametrize` instead of copy-pasted tests, and `tmp_path` for file I/O.
- Cover edge cases that matter: an empty doc, a single doc, repeated tokens, zero vectors, ties when clustering.
- Type-hint test functions (`-> None`). Don't mock unless I/O forces it.
- These tests also feed `test-cases.txt` (4 pts): each of the 4 major steps (preprocessing, vectorization, similarity, clustering) needs clear input → output cases.

## Good vs. bad
| Good | Bad |
|---|---|
| Fails if the code is wrong | Passes on broken code |
| Checks behaviour/output | Checks internals or call counts |
| Deterministic, fast | Random, slow, order-dependent |
| One idea per test | Duplicates another test |

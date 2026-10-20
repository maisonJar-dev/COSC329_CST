---
name: engineer
description: Coding standards for this repo. Use whenever writing, editing, or reviewing Python in src/.
---
## Standards
- Python 3, run in `.venv`. Type hints on every function signature and return.
- Must be ruff-clean (lint + format). Use snake_case, and name things for what they hold (`doc_vectors`, not `dv`).
- Use pydantic only where data crosses a boundary (loading files, outputs). Use plain types and dataclasses internally.
- One responsibility per function. Folder roles:
  - `preprocessing/`: sanitizing text
  - `vectorization/`: TF, IDF, TF-IDF
  - `helpers/`: similarity, clustering, I/O
- Write pure functions where possible (input → output, no hidden state) so they're easy to test.
- Use numpy for vector maths once the loops get hot. Correctness comes first, then clarity, then speed.
- Docstrings: one line, only when the name isn't enough. No comment clutter.

## Rubric constraint (4 pts)
No bloat: no CLI flags, config options, plug-in points, "future-proof" abstractions, or unused helpers. Build exactly what the assignment needs. Before adding anything, ask: "Does a rubric item need this?"

## When unsure
Prefer the simpler design and explain the trade-off rather than building flexibility.

---
name: evaluate-tests
description: Check test coverage for src/, write missing pytest tests, grade existing tests, and log to logs/test-eval.md.
disable-model-invocation: true
argument-hint: "[folder or file]"
---
Launch the `evaluate-tests` agent. Scope: $ARGUMENTS (if empty, all of `src/`).

When it finishes, show me the pytest result line, which test files were added, the bad tests it found, and any source bugs. Don't paste the whole log.

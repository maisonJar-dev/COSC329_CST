# Command cheat sheet

## Slash commands (manual)
| Command | Args | Does | Output |
|---|---|---|---|
| `/check-rubric` | none | Audits repo (incl. uncommitted) against `grading_criteria_texts/criteria.md`, estimates mark /19 | `logs/rubric-status.md` |
| `/evaluate-tests` | `[folder or file]` (default `src/`) | Finds untested modules, writes pytest tests, grades existing ones, runs suite | `logs/test-eval.md` |
| `/senior-review` | `[file, commit, or range]` (default staged → unstaged → HEAD) | In-depth code review | `logs/senior_review/` |
| `/cpp-teaching` | `<topic>` (empty = next in curriculum) | C++ lesson tied to `src/` and the Mini-Copilot | `logs/learn_cpp/` |

## Auto-loaded skills
- `engineer`: Python standards for `src/`
- `python-tests`: pytest conventions for `src/tests/`

## After a push
1. `/evaluate-tests`
2. `/senior-review`
3. `/check-rubric`
4. `/cpp-teaching`

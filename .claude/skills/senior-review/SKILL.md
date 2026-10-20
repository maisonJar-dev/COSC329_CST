---
name: senior-review
description: Run an in-depth senior-engineer review of current changes and log it to logs/senior_review/.
disable-model-invocation: true
argument-hint: "[file, commit, or range]"
---
Launch the `senior-engineer-review` agent. Target: $ARGUMENTS (if empty, the agent picks staged changes, then unstaged changes, then HEAD).

When it finishes, give me the verdict line, the top 3 improvements, and the path to the log file. Don't paste the whole review.

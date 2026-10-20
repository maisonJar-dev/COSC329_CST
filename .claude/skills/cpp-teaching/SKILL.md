---
name: cpp-teaching
description: Get an on-demand C++ lesson on a chosen topic, logged to logs/learn_cpp/.
disable-model-invocation: true
argument-hint: "<topic, e.g. templates, CMake, smart pointers, move semantics>"
---
Launch the `cpp-teacher` agent with this topic instead of a push diff: $ARGUMENTS

If the topic is empty, ask the agent to pick the next topic in its curriculum based on the existing lessons in `logs/learn_cpp/`.

When it finishes, give me the lesson title, the exercise, and the log path.

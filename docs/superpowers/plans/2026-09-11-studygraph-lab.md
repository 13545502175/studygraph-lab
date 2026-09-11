# StudyGraph Lab Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a local Python CLI that validates learning graphs, ranks review priorities, and renders an HTML report.

**Architecture:** A small `studygraph` package separates IO, graph validation, recommendation, reporting, and CLI orchestration. JSON/CSV data flows through validated dictionaries into a deterministic scoring engine and HTML renderer.

**Tech Stack:** Python 3.10+, standard library, pytest, GitHub Actions.

## Global Constraints

- No cloud API or paid dependency.
- Support CSV and JSON input with `id`, `name`, `prerequisites`, `mastery`.
- CLI commands: `validate`, `recommend`, `report`.

### Task 1: Package and data layer
Create `studygraph/__init__.py`, `studygraph/io.py`, `studygraph/graph.py`, and sample data. Implement `load_nodes(path)`, `validate_nodes(nodes)`, and `build_graph(nodes)` with cycle detection and clear `ValueError` messages. Add tests for JSON, CSV, unknown prerequisite, and cycle.

### Task 2: Recommendation engine
Create `studygraph/recommend.py` with `recommend(nodes, graph, limit=None)` returning ranked dictionaries containing score components and explanation. Add tests for deterministic ordering and mastery effects.

### Task 3: Report and CLI
Create `studygraph/report.py` and `studygraph/cli.py`; expose `python -m studygraph`. Implement the three commands, JSON output, and self-contained HTML. Add CLI smoke tests.

### Task 4: Documentation and CI
Create README, pyproject.toml, LICENSE, and `.github/workflows/test.yml`. Run the full test suite and a sample report command, then commit all work.

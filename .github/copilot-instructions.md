# Copilot Instructions for COMP110 Workspace

## Project Overview
- This workspace is for the UNC COMP110 Fall 2025 course. It contains lessons, exercises, coding questions (CQs), and tools for student programming practice and assessment.
- Major directories:
  - `exercises/`: Individual Python exercises (e.g., `ex00_hello_world.py`, `ex02_wordle.py`).
  - `CQs/`: Coding questions for practice and assessment (e.g., `cq00_conditionals.py`).
  - `lessons/`: Example scripts for learning concepts (e.g., `functions.py`).
  - `tools/`: Helper scripts for grading, submission, or utility functions (e.g., `helpers.py`, `submission.py`).
  - `data/`: Datasets for exercises (e.g., baby names CSVs).

## Key Patterns & Conventions
- Each Python file typically includes a module docstring and an `__author__` variable for attribution.
- Most scripts are designed to be run directly (contain `if __name__ == "__main__": ...`).
- Exercise and CQ files are self-contained; avoid cross-imports between them unless specified.
- Use type annotations for variables and function signatures (e.g., `def foo(x: int) -> str:`).
- Follow PEP8 style, but prioritize clarity for beginners.

## Workflows
- **Backup:** Use VS Code Source Control to commit and push changes to your personal GitHub repo (`backup` remote).
- **Update Materials:** Use VS Code Command Palette to pull from `origin/main` for new course content.
- **Run Code:** Execute scripts directly in the terminal (e.g., `python exercises/ex02_wordle.py`).
- **No build step** is required; this is a pure Python project.
- **Testing:** No formal test suite; verify correctness by running scripts and checking output.

## Integration & Dependencies
- All code is standard Python 3.12+; external dependencies (if any) are listed in `requirements.txt`.
- Data files are read from the `data/` directory using relative paths.
- Tools in `tools/` may be used for grading or submission automation.

## Examples
- To run a CQ: `python CQs/cq00_conditionals.py`
- To run an exercise: `python exercises/ex01_tea_party.py`

## Special Notes
- Do not introduce frameworks or complex dependencies.
- Keep code beginner-friendly and well-commented.
- When adding new exercises or CQs, follow the naming and structure conventions in their respective folders.

---
For more details, see `README.md`.

# python-workout

A Python project for practicing and improving Python programming skills.

**Requirements:** Python 3.14+

## Structure

- `src/python_workout_pkg/numeric/` — Exercises package
  - `number_guessing_game.py` — Number guessing (unlimited or limited attempts)
  - `number_and_base_guessing_game.py` — Number guessing in base 2, 8, 10, or 16
  - `guessing_word_game.py` — Word guessing with min/max length and dictionary hints
  - `summing_numbers.py` — `Numbers` (mysum, mean, sum_integers) and `Words` (words_analyzer) helpers
- `tests/` — Unit tests for the numeric exercises

## Setup

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Install dependencies (includes dev: ruff, pre-commit)
uv sync
```

### Pre-commit (optional)

```bash
pre-commit install   # Ruff lint + format on commit
```

## Run

```bash
# Number guessing game
python -m python_workout_pkg.numeric.number_guessing_game

# Number guessing in random base
python -m python_workout_pkg.numeric.number_and_base_guessing_game

# Word guessing game
python -m python_workout_pkg.numeric.guessing_word_game

# Summing numbers examples
python -m python_workout_pkg.numeric.summing_numbers
```

## Test

```bash
uv run pytest
```
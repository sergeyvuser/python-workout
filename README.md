# python-workout

A Python project for practicing and improving Python programming skills.

**Requirements:** Python 3.14+

## Structure

- `numeric/` — Exercises module
  - `number_guessing_game.py` — Number guessing (unlimited or limited attempts)
  - `number_and_base_guessing_game.py` — Number guessing in base 2, 8, 10, or 16
  - `guessing_word_game.py` — Word guessing with min/max length and dictionary hints
  - `summing_numbers.py` — Summing function `mysum(*numbers, start=0)` with optional start

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
python -m numeric.number_guessing_game

# Number guessing in random base
python -m numeric.number_and_base_guessing_game

# Word guessing game
python -m numeric.guessing_word_game

# Summing numbers examples
python -m numeric.summing_numbers
```
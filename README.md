# python-workout

A Python project for practicing and improving Python programming skills.

## Structure

- `numeric/` - Exercises module
  - `number_guessing_game.py` - Number guessing game (unlimited or limited attempts)
  - `number_and_base_guessing_game.py` - Number guessing in a random base (2, 8, 10, 16)
  - `guessing_word_game.py` - Word guessing with min/max length and dictionary hints
  - `summing_numbers.py` - Summing functions (`mysum`, `mysum2`)

## Setup

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Install dependencies (including dev: ruff)
uv sync
```

### Pre-commit (optional)

```bash
# Install pre-commit hooks (Ruff lint + format)
pre-commit install
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
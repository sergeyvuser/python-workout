# python-workout

A Python project for practicing and improving Python programming skills.

## Structure

- `numeric/` - Numeric exercises module
  - `number_guessing_game.py` - Number guessing game implementation
  - `summing_numbers.py` - Summing functions implementation

## Setup

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Install dependencies
uv pip install -e .
```

## Run

```bash
# Run number guessing game
python -m numeric.number_guessing_game

# Run summing numbers examples
python -m numeric.summing_numbers
```
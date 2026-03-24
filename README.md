# python-workout

A Python project for practicing and improving Python programming skills.

**Requirements:** Python 3.14+

## Structure

- `src/python_workout_pkg/exercises/` - Exercises package
- `src/python_workout_pkg/exercises/numeric/` - Numeric exercises
- `src/python_workout_pkg/exercises/strings/` - String exercises
- `src/python_workout_pkg/shared/cli/` - Shared CLI helpers
- `src/python_workout_pkg/base.py` - Exercise base class
- `src/python_workout_pkg/exercise_registry.py` - Exercise registry
- `src/python_workout_pkg/main.py` - Interactive menu entrypoint
- `tests/` - Unit tests

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
# Interactive menu
workout

# Or via module
python -m python_workout_pkg.main

# Run individual exercises directly
python -m python_workout_pkg.exercises.numeric.number_guessing_game
python -m python_workout_pkg.exercises.numeric.number_and_base_guessing_game
python -m python_workout_pkg.exercises.numeric.guessing_word_game
python -m python_workout_pkg.exercises.numeric.summing_numbers
python -m python_workout_pkg.exercises.numeric.run_timing
python -m python_workout_pkg.exercises.numeric.hexadecmal_output
python -m python_workout_pkg.exercises.numeric.name_triangle
python -m python_workout_pkg.exercises.numeric.float_numbers_transform
python -m python_workout_pkg.exercises.strings.pig_latin.pig_latin_new
```

## Test

```bash
uv run pytest
# With coverage
uv run pytest --cov
```

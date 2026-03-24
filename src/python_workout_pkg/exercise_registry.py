from python_workout_pkg.exercise_models import ExerciseMeta
from python_workout_pkg.base import Exercise

# registry of all exercises id -> (meta, ExerciseClass)
_registry: dict[str, tuple[ExerciseMeta, type[Exercise]]] = {}


def register(meta: ExerciseMeta):
    """Class decorator to register an Exercise in the global registry."""

    def decorator(cls: type[Exercise]) -> type[Exercise]:
        _registry[meta.id] = (meta, cls)
        return cls

    return decorator


def get_all() -> list[tuple[ExerciseMeta, type[Exercise]]]:
    """Return all registered exercises sorted by id."""
    return sorted(_registry.values(), key=lambda pair: pair[0].id)

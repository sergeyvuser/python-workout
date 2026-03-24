from abc import ABC, abstractmethod


class Exercise(ABC):
    """Base class for all workout exercises."""

    @classmethod
    @abstractmethod
    def run(cls) -> None:
        """Run the interactive exercise logic."""
        ...

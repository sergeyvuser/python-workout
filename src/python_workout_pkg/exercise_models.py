from pydantic import BaseModel


class ExerciseMeta(BaseModel):
    id: str  # e.g. "ch01-e01"
    title: str  # e.g. "Сложение чисел"
    chapter: str  # e.g. "Chapter 1: Numbers"
    description: str  # short description shown in the menu

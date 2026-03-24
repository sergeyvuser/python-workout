"""
Pig Latin converter module.

Pig Latin is a language game where words are transformed according to simple rules:
- Words beginning with a vowel add 'way' to the end
- Words beginning with a consonant move the first letter to the end and add 'ay'
"""

import string

from typing import ClassVar

from pydantic import BaseModel, computed_field, field_validator, Field

from python_workout_pkg.shared.cli import CLIInputHandler, collect_input
from python_workout_pkg.base import Exercise
from python_workout_pkg.exercise_models import ExerciseMeta
from python_workout_pkg.exercise_registry import register


@register(
    ExerciseMeta(
        id="ch02-e05-06",
        title="Pig Latin words and phrases",
        chapter="Chapter 3: Strings",
        description="Convert a word or phrase to Pig Latin. e.g. 'hello' -> 'ellohay'",
    )
)
class PigLatin(BaseModel, Exercise):
    VOWELS: ClassVar[str] = "aeiou"
    SUFFIX_VOWEL: ClassVar[str] = "way"
    SUFFIX_CONSONANT: ClassVar[str] = "ay"
    MAX_INPUT_LENGTH: ClassVar[int] = 500

    initial_input: str = Field(
        description="The word or sentence to convert to Pig Latin",
        title="Initial Input",
        max_length=MAX_INPUT_LENGTH,
    )

    @field_validator("initial_input")
    @classmethod
    def validate_initial_input(cls, v: str) -> str:
        """
        Validates the input.

        Args:
            v: The word or sentence to validate

        Returns:
            str: The validated input

        Raises:
            ValueError: If the input is empty or contains no words.
        """
        v = v.strip()
        if not v:
            raise ValueError("Input is empty. Please enter a valid word or phrase.")

        if not v.split():
            raise ValueError(
                "Input contains no words. Please enter a valid word or phrase."
            )

        return v

    @computed_field
    @property
    def pig_latin(self) -> str:
        return " ".join(
            self._translate_word(word) for word in self.initial_input.split()
        )

    def _translate_word(self, word: str) -> str:
        """Orchestrates punctuation stripping, translation, and reassembly."""
        prefix_punct, core, suffix_punct = self._split_punctuation(word)

        if not core:
            return word  # punctuation-only token, return as-is

        translated = self._apply_pig_latin_rules(core)
        translated = self._capitalize_if_needed(core, translated)
        return prefix_punct + translated + suffix_punct

    def _split_punctuation(self, word: str) -> tuple[str, str, str]:
        """Splits a word into prefix, core, and suffix punctuation."""
        core = word.strip(string.punctuation)
        prefix_punct = word[: len(word) - len(word.lstrip(string.punctuation))]
        suffix_punct = word[len(word.rstrip(string.punctuation)) :]
        return prefix_punct, core, suffix_punct

    def _apply_pig_latin_rules(self, word: str) -> str:
        """Applies Pig Latin transformation rules to a clean (no punctuation) word."""
        lower_word = word.lower()

        vowel_index = next(
            (i for i, char in enumerate(lower_word) if char in self.VOWELS), None
        )

        if vowel_index == 0:
            return word + self.SUFFIX_VOWEL
        elif vowel_index is not None:
            return word[vowel_index:] + word[:vowel_index] + self.SUFFIX_CONSONANT
        else:
            return word + self.SUFFIX_CONSONANT

    def _capitalize_if_needed(self, original: str, transformed: str) -> str:
        """Capitalizes the first letter of transformed if original was capitalized."""
        if original[0].isupper():
            return transformed[0].upper() + transformed[1:]
        return transformed

    def _multi_vowel_check(self, word: str) -> str:
        """Applies Pig Latin transformation rules to a word with multiple vowels."""
        number_vowels = len(set(word.lower()) & set(self.VOWELS))

        if number_vowels > 1:
            return word + self.SUFFIX_VOWEL
        else:
            return word + self.SUFFIX_CONSONANT

    @classmethod
    def run(cls) -> None:
        def collector() -> dict:
            return collect_input(
                prompt="Enter a word or phrase: ",
                transformer=lambda raw: {"initial_input": raw},
            )

        handler = CLIInputHandler(
            model=cls,
            collector=collector,
            session_description="To convert a word or phrase to Pig Latin, enter your text",
            formatter=lambda instance: f"Pig Latin: {instance.pig_latin}",
        )
        handler.run_input_session()


if __name__ == "__main__":
    PigLatin.run()

"""
Tests for the PigLatinWord module.

Tests cover:
- Pig Latin conversion (vowels, consonants, edge cases)
- Pydantic field validation (empty, too long, phrases)
- computed_field for pig_latin
- print_results output
- model_dump serialization
"""

import pytest
from pydantic import ValidationError
from python_workout_pkg.exercises.strings.pig_latin import PigLatin


class TestPigLatinWord:
    """
    Tests for the PigLatinWord class.
    """

    # =============================================================================
    # Test Data
    # =============================================================================

    # Words starting with vowels → add 'way'
    vowel_words_testdata = [
        ("apple", "appleway"),
        ("orange", "orangeway"),
        ("umbrella", "umbrellaway"),
        ("elephant", "elephantway"),
        ("igloo", "iglooway"),
        ("aeiou", "aeiouway"),
    ]

    # Words starting with consonants → move first letter + 'ay'
    consonant_words_testdata = [
        ("hello", "ellohay"),
        ("python", "onpythay"),
        ("world", "orldway"),
        ("test", "esttay"),
        ("code", "odecay"),
        ("string", "ingstray"),
    ]

    # Words with uppercase letters
    uppercase_vowel_testdata = [
        ("Apple", "Appleway"),
        ("Orange", "Orangeway"),
        ("Umbrella", "Umbrellaway"),
        ("ELEPHANT", "ELEPHANTway"),
    ]

    uppercase_consonant_testdata = [
        ("Hello", "ElloHay"),
        ("Python", "OnPythay"),
        ("World", "OrldWay"),
        ("TEST", "ESTTay"),  # suffix 'ay' is always lowercase
    ]

    # Short words
    short_words_testdata = [
        ("a", "away"),
        ("i", "iway"),
        ("I", "Iway"),
        ("A", "Away"),
        ("o", "oway"),
        ("u", "uway"),
    ]

    # =============================================================================
    # Conversion Tests - Vowel Words
    # =============================================================================

    @pytest.mark.parametrize("word, expected", vowel_words_testdata)
    def test_convert_word_starting_with_vowel(self, word, expected):
        """Test words starting with lowercase vowels add 'way' suffix."""
        pig_latin = PigLatin(initial_input=word)
        assert pig_latin.pig_latin == expected

    @pytest.mark.parametrize("word, expected", uppercase_vowel_testdata)
    def test_convert_word_starting_with_uppercase_vowel(self, word, expected):
        """Test words starting with uppercase vowels preserve case and add 'way'."""
        pig_latin = PigLatin(initial_input=word)
        assert pig_latin.pig_latin == expected

    # =============================================================================
    # Conversion Tests - Consonant Words
    # =============================================================================

    @pytest.mark.parametrize("word, expected", consonant_words_testdata)
    def test_convert_word_starting_with_consonant(self, word, expected):
        """Test words starting with lowercase consonants move first letter + 'ay'."""
        pig_latin = PigLatin(initial_input=word)
        assert pig_latin.pig_latin == expected

    @pytest.mark.parametrize("word, expected", uppercase_consonant_testdata)
    def test_convert_word_starting_with_uppercase_consonant(self, word, expected):
        """Test words starting with uppercase consonants preserve case pattern."""
        pig_latin = PigLatin(initial_input=word)
        assert pig_latin.pig_latin == expected

    # =============================================================================
    # Conversion Tests - Short Words
    # =============================================================================

    @pytest.mark.parametrize("word, expected", short_words_testdata)
    def test_convert_short_words(self, word, expected):
        """Test single letter words are handled correctly."""
        pig_latin = PigLatin(initial_input=word)
        assert pig_latin.pig_latin == expected

    # =============================================================================
    # Field Validation Tests
    # =============================================================================

    def test_empty_string_raises_error(self):
        """Test that empty string raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            PigLatin(initial_input="")

        assert "Input is empty. Please enter a valid word or phrase." in str(
            exc_info.value
        )

    def test_whitespace_only_raises_error(self):
        """Test that whitespace-only string raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            PigLatin(initial_input="   ")

        assert "Input is empty. Please enter a valid word or phrase." in str(
            exc_info.value
        )

    def test_too_long_raises_error(self):
        """Test that input longer than 500 characters raises ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            PigLatin(initial_input="a" * 501)
        assert "String should have at most 500 characters" in str(exc_info.value)

    def test_exactly_500_chars_is_accepted(self):
        """Test that input of exactly 500 characters is accepted."""
        word = "a" * 500
        pig_latin = PigLatin(initial_input=word)
        assert pig_latin.initial_input == word
        assert pig_latin.pig_latin == "a" * 500 + "way"

    # =============================================================================
    # Punctuation Tests
    # =============================================================================

    def test_word_with_suffix_punctuation(self):
        """Test that trailing punctuation is stripped before translation and reattached."""
        pig_latin = PigLatin(initial_input="hello!")
        assert pig_latin.pig_latin == "ellohay!"

    def test_word_with_prefix_punctuation(self):
        """Test that leading punctuation is stripped before translation and reattached."""
        pig_latin = PigLatin(initial_input="...air")
        assert pig_latin.pig_latin == "...airway"

    def test_word_with_prefix_and_suffix_punctuation(self):
        """Test that both leading and trailing punctuation are preserved."""
        pig_latin = PigLatin(initial_input='"hello"')
        assert pig_latin.pig_latin == '"ellohay"'

    def test_punctuation_only_token_returned_as_is(self):
        """Test that a punctuation-only token is returned unchanged."""
        pig_latin = PigLatin(initial_input="--")
        assert pig_latin.pig_latin == "--"

    # =============================================================================
    # Edge Cases and Additional Tests
    # =============================================================================

    def test_mixed_case_word_consonant(self):
        """Test mixed case word starting with consonant."""
        pig_latin = PigLatin(initial_input="HeLLo")
        assert pig_latin.pig_latin == "ELLoHay"

    def test_mixed_case_word_vowel(self):
        """Test mixed case word starting with vowel capitalizes correctly."""
        pig_latin = PigLatin(initial_input="ApPlE")
        assert pig_latin.pig_latin == "ApPlEway"

    def test_word_with_numbers(self):
        """Test word containing numbers processes alphabetic part correctly."""
        pig_latin = PigLatin(initial_input="test123")
        assert pig_latin.pig_latin == "est123tay"

    def test_single_consonant(self):
        """Test single consonant letter with no vowel adds 'ay'."""
        pig_latin = PigLatin(initial_input="b")
        assert pig_latin.pig_latin == "bay"

    def test_all_vowels_word(self):
        """Test word consisting of all vowels adds 'way'."""
        pig_latin = PigLatin(initial_input="aeiou")
        assert pig_latin.pig_latin == "aeiouway"

    # =============================================================================
    # Pydantic Serialization Tests
    # =============================================================================

    def test_model_dump(self):
        """Test model_dump() serialization uses correct field names."""
        pig_latin = PigLatin(initial_input="hello")
        dump = pig_latin.model_dump()
        assert dump == {
            "initial_input": "hello",
            "pig_latin": "ellohay",
        }

    def test_model_dump_json(self):
        """Test model_dump_json() serialization uses correct field names."""
        pig_latin = PigLatin(initial_input="hello")
        json_dump = pig_latin.model_dump_json()
        assert '"initial_input":"hello"' in json_dump
        assert '"pig_latin":"ellohay"' in json_dump

    def test_model_validate_after_validation_error(self):
        """Test that model_validate rejects invalid values and original instance is unaffected."""
        pig_latin = PigLatin(initial_input="hello")
        assert pig_latin.initial_input == "hello"

        with pytest.raises(ValidationError):
            pig_latin.model_validate({"initial_input": ""})

        assert pig_latin.initial_input == "hello"
        assert pig_latin.pig_latin == "ellohay"

    def test_class_variables_accessible(self):
        """Test that class variables (constants) are accessible on the class."""
        assert PigLatin.VOWELS == "aeiou"
        assert PigLatin.SUFFIX_VOWEL == "way"
        assert PigLatin.SUFFIX_CONSONANT == "ay"
        assert PigLatin.MAX_INPUT_LENGTH == 500

    def test_class_variables_not_in_model_dump(self):
        """Test that ClassVar fields are not included in model dump."""
        pig_latin = PigLatin(initial_input="hello")
        dump = pig_latin.model_dump()

        # ClassVar should not be in model dump
        assert "VOWELS" not in dump
        assert "SUFFIX_VOWEL" not in dump
        assert "SUFFIX_CONSONANT" not in dump
        assert "MAX_INPUT_LENGTH" not in dump


class TestPigLatinSentence:
    """
    Tests for sentence translation via the PigLatin class.
    """

    # =============================================================================
    # Test Data
    # =============================================================================

    sentence_testdata = [
        (
            "this is a test translation",
            "isthay isway away esttay anslationtray",
        ),
        (
            "python is an amazing language",
            "onpythay isway anway amazingway anguagelay",
        ),
        (
            "every expert was once a beginner",
            "everyway expertway asway onceway away eginnerbay",
        ),
    ]

    # =============================================================================
    # Sentence Conversion Tests
    # =============================================================================

    @pytest.mark.parametrize("sentence, expected", sentence_testdata)
    def test_convert_sentence(self, sentence, expected):
        """Test full sentence conversion to Pig Latin."""
        pig_latin = PigLatin(initial_input=sentence)
        assert pig_latin.pig_latin == expected

    def test_single_word_sentence(self):
        """Test that a single word sentence behaves identically to a word."""
        pig_latin = PigLatin(initial_input="hello")
        assert pig_latin.pig_latin == "ellohay"

    def test_sentence_preserves_word_count(self):
        """Test that output has the same number of words as input."""
        sentence = "this is a test"
        pig_latin = PigLatin(initial_input=sentence)
        assert len(pig_latin.pig_latin.split()) == len(sentence.split())

    def test_sentence_with_punctuation(self):
        """Test that punctuation is preserved in sentence translation."""
        pig_latin = PigLatin(initial_input="hello, world!")
        assert pig_latin.pig_latin == "ellohay, orldway!"

    def test_sentence_with_capitalized_first_word(self):
        """Test that a capitalized first word is handled correctly in a sentence."""
        pig_latin = PigLatin(initial_input="Hello world")
        assert pig_latin.pig_latin == "ElloHay orldway"

    def test_sentence_model_dump(self):
        """Test model_dump for sentence input includes initial_input and pig_latin."""
        pig_latin = PigLatin(initial_input="hello world")
        dump = pig_latin.model_dump()
        assert dump["initial_input"] == "hello world"
        assert dump["pig_latin"] == "ellohay orldway"

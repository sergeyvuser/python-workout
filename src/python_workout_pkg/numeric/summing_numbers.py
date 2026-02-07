class Numbers:
    """Numbers class with summing function"""

    def __init__(self, *numbers):
        """
        Args:
            *numbers: iterable of any type of numbers to sum (can be int or float)
        """
        self.numbers = numbers

    def mysum(self, start: int = 10) -> int:
        """
        Summing function with start parameter

        Args:
            start: start value
        Returns:
            sum of numbers + start
        """
        summ = start
        for number in self.numbers:
            summ += number
        return summ

    @staticmethod
    def is_intable(item) -> bool:
        """
        Check if item is intable
        Args:
            item: object of any type
        Returns:
            True if item is intable, False otherwise
        """
        try:
            int(item)
            return True
        except ValueError:
            return False
        except TypeError:
            return False

    def sum_integers(self) -> int:
        """
        Summing only objects which are either integers or can be converted to integers
        Returns:
            sum of only integers in numbers
        """
        if not self.numbers:
            return 0

        return sum(int(item) for item in self.numbers if self.is_intable(item))

    def mean(self) -> float | None:
        """
        Mean function
        Returns:
            mean of numbers
        """
        if len(self.numbers) == 0:
            return None

        summ = 0
        for number in self.numbers:
            summ += number

        return summ / len(self.numbers)


class Words:
    def __init__(self, *words: list[str]):
        """
        Args:
            *words: list of words to analyze
        """
        self.words = words

    def words_analyzer(self) -> tuple[int, int, float]:
        if not self.words:
            return 0, 0, 0.0
        word_lengths = [len(word) for word in self.words]
        return (
            min(word_lengths),
            max(word_lengths),
            sum(word_lengths) / len(word_lengths),
        )

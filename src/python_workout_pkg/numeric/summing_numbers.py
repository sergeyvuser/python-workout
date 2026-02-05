class Numbers:
    """Numbers class with summing function"""

    def __init__(self, *numbers):
        """
        Args:
            *numbers: numbers to sum
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

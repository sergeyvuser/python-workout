class Numbers:
    """Numbers class with summing function"""

    def __init__(self, *numbers):
        """
        Args:
            *numbers: numbers to sum
        """
        self.numbers = numbers

    def mysum(self, start: int = 0) -> int:
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
        assert self.words, "No words provided"
        word_lengths = [len(word) for word in self.words]
        return (
            min(word_lengths),
            max(word_lengths),
            sum(word_lengths) / len(word_lengths),
        )


if __name__ == "__main__":
    num1 = Numbers(10, 20, 30, 40)
    num2 = Numbers(*[1, 2, 3, 4, 5])
    num3 = Numbers(*range(1, 101))
    num4 = Numbers()
    num5 = Numbers(0)
    print(num1.mysum(), num1.mean())
    print(num1.mysum(10), num1.mean())
    print(num2.mysum(0), num2.mean())
    print(num3.mysum(), num3.mean())
    print(num3.mysum(10), num3.mean())
    print(num4.mysum(), num4.mean())
    print(num4.mysum(10), num4.mean())
    print(num5.mysum(), num4.mean())
    print(num5.mysum(10), num4.mean())

    words1 = Words("apple", "banana", "cherry", "date", "elderberry")
    words2 = Words("fig", "grape", "honeydew", "kiwi", "lemon")
    words3 = Words("mango", "nectarine", "orange", "papaya", "quince")
    words4 = Words("raspberry", "strawberry", "tomato", "ugli", "violet")
    words5 = Words("watermelon", "xigua", "yellow", "zucchini")
    print(words1.words_analyzer())
    print(words2.words_analyzer())
    print(words3.words_analyzer())
    print(words4.words_analyzer())
    print(words5.words_analyzer())

    words6 = Words()
    print(words6.words_analyzer())
    words7 = Words("")
    print(words7.words_analyzer())

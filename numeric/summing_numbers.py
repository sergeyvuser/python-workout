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


if __name__ == "__main__":
    sum_test1 = Numbers(10, 20, 30, 40)
    sum_test2 = Numbers(*[1, 2, 3, 4, 5])
    sum_test3 = Numbers(*range(1, 101))
    print(sum_test1.mysum())
    print(sum_test1.mysum(10))
    print(sum_test2.mysum(0))
    print(sum_test3.mysum())
    print(sum_test3.mysum(10))

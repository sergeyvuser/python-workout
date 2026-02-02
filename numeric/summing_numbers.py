class Sum:
    def mysum(*numbers, start: int = 0) -> int:
        """
        Summing function with start parameter

        Args:
            *numbers: numbers to sum
            start: start value
        Returns:
            sum of numbers + start
        """
        summ = start
        for number in numbers:
            summ += number
        return summ


if __name__ == "__main__":
    sum_test = Sum()
    print(sum_test.mysum(10, 20, 30, 40))
    print(sum_test.mysum(10, 20, 30, 40, start=10))
    print(sum_test.mysum(*[1, 2, 3, 4, 5], start=0))
    print(sum_test.mysum(*range(1, 101)))
    print(sum_test.mysum(*range(1, 101), start=10))

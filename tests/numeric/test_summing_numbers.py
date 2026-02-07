import pytest
from python_workout_pkg.numeric.summing_numbers import Numbers, Words

testdata = [
    ((1, 2, 3, 4, 5), None, 25),
    ((1, 2, 3, 4, 5), 10, 25),
    ((1, 2, 3, 4, 5), 0, 15),
    ([10, 20, 30], None, 70),
    ([10, 20, 30], 10, 70),
    ([10, 20, 30], 0, 60),
    (range(1, 101), None, 5060),
    (range(1, 101), 10, 5060),
    (range(1, 101), 0, 5050),
    ((), None, 10),
    ((), 10, 10),
    ((), 0, 0),
    ((0,), None, 10),
    ((0,), 10, 10),
    ((0,), 0, 0),
]

testdata_mean = [
    ((1, 2, 3, 4, 5), 3),
    ((1, 2, 3, 4, 5), 3),
    ((1, 2, 3, 4, 5), 3),
    ([10, 20, 30], 20),
    ([10, 20, 30], 20),
    ([10, 20, 30], 20),
    (range(1, 101), 50.5),
    (range(1, 101), 50.5),
    (range(1, 101), 50.5),
    ((), None),
    ((), None),
    ((), None),
    ((0,), 0),
    ((0,), 0),
    ((0,), 0),
]

testdata_integers = [
    ((1, 2, "hello", 4, 5), 12),
    ((1, 2, 3.0, 4, 5), 15),
    ((1, 2, 3, 4.5, 5), 15),
    ((1, 2, None, 4, 5), 12),
    ([10, "hello", 30], 40),
    ([10, "10", 30], 50),
    ([10, (), 30], 40),
    ([10, [], 30], 40),
    (range(1, 101), 5050),
    (("",), 0),
    ((10,), 10),
    (("10",), 10),
    ((), 0),
    ((0,), 0),
    ({0}, 0),
    ({}, 0),
    ({"10"}, 10),
    ({10}, 10),
    ({"hello"}, 0),
    ({None}, 0),
]


class TestNumbers:
    @pytest.mark.parametrize("numbers, start, result", testdata)
    def test_mysum(self, numbers, start, result):
        number = Numbers(*numbers)
        if start is None:
            assert number.mysum() == result
        else:
            assert number.mysum(start) == result

    @pytest.mark.parametrize("numbers, result", testdata_mean)
    def test_mean(self, numbers, result):
        assert Numbers(*numbers).mean() == result

    @pytest.mark.parametrize("numbers, result", testdata_integers)
    def test_sum_integers(self, numbers, result):
        assert Numbers(*numbers).sum_integers() == result


testdata_words = [
    (("apple", "banana", "cherry", "date", "elderberry"), 4, 10, 6.2),
    (("fig", "grape", "honeydew", "kiwi", "lemon"), 3, 8, 5.0),
    (("mango", "nectarine", "orange", "papaya", "quince"), 5, 9, 6.4),
    (("raspberry", "strawberry", "tomato", "ugli", "violet"), 4, 10, 7.0),
    (("watermelon", "xigua", "yellow", "zucchini"), 5, 10, 7.25),
    ((), 0, 0, 0.0),
    (("",), 0.0, 0, 0.0),
    (("apple",), 5, 5, 5),
    (("fig", "grape"), 3, 5, 4.0),
    (("mango", "nectarine", "date"), 4, 9, 6.0),
]


class TestWords:
    @pytest.mark.parametrize("words, min_len, max_len, average_len", testdata_words)
    def test_words_analyzer(self, words, min_len, max_len, average_len):
        assert Words(*words).words_analyzer() == (min_len, max_len, average_len)

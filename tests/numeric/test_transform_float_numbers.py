import pytest
from python_workout_pkg.numeric.float_numbers_transform import transform_float_numbers

testdata = [
    (0.0, 0, 0, None),
    (0.1, 0, 0, None),
    (0.1, 1, 0, 0.0),
    (0.1, 1, 1, 0.1),
    (0.1, 1, 2, 0.1),
    (0.1, 0, 1, 0.1),
    (1.1, 2, 2, 1.1),
    (1234.1234, 0, 0, None),
    (1234.1234, 1, 0, 4.0),
    (1234.1234, 2, 0, 34.0),
    (1234.1234, 3, 0, 234.0),
    (1234.1234, 4, 0, 1234.0),
    (1234.1234, 0, 1, 0.1),
    (1234.1234, 0, 2, 0.12),
    (1234.1234, 0, 3, 0.123),
    (1234.1234, 0, 4, 0.1234),
    (1234.1234, 5, 5, 1234.1234),
    (1234.1234, -1, -1, 1234.1234),
    (1234.1234, -1, 0, 1234.0),
    (1234.1234, 0, -1, 0.1234),
    (0.2323, 1, 100, 0.2323),
    (0.2323, 1, 2, 0.23),
    (0.2323, 2, 1, 0.2),
    (0.2323, 2, 2, 0.23),
    (0.2323, 2, 3, 0.232),
    (0.2323, 2, 4, 0.2323),
    (0.2323, 2, 5, 0.2323),
]


@pytest.mark.parametrize("float_number, before_dot, after_dot, result", testdata)
def test_transform_float_numbers(float_number, before_dot, after_dot, result):
    assert transform_float_numbers(float_number, before_dot, after_dot) == result

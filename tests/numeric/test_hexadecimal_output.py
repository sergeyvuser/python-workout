import pytest
from python_workout_pkg.numeric.hexadecmal_output import Hexs


class TestHexs:
    """
    Tests for the Hexs class.
    """

    hexs_testdata = [
        ("10", 16),
        ("1A", 26),
        ("1a", 26),
        ("1B", 27),
        ("1F", 31),
        ("0", 0),
        ("00", 0),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("9", 9),
        ("A", 10),
        ("B", 11),
        ("C", 12),
        ("D", 13),
        ("E", 14),
        ("F", 15),
    ]

    invalid_hexs_testdata = ["", None, "G", "g", "asdgfaergv", "1G", "1G1", "/>,."]

    def test_print_results_no_hex_num(self, monkeypatch, capsys):
        new_hex = Hexs()
        new_hex.print_results()
        captured = capsys.readouterr()
        assert "No hexadecimal number entered." in captured.out
        assert captured.err == ""
        assert new_hex.hex_num is None
        assert new_hex.dec_num is None

    @pytest.mark.parametrize("input_string, expected_dec_num", hexs_testdata)
    def test_input_str_handler_with_valid_input(
        self, input_string, expected_dec_num, capsys
    ):
        new_hex = Hexs()
        new_hex.input_str_handler(input_string)
        captured = capsys.readouterr()
        assert f"Decimal number: {expected_dec_num}" in captured.out
        assert captured.err == ""
        assert new_hex.dec_num == expected_dec_num
        assert new_hex.hex_num == input_string

    @pytest.mark.parametrize("input_string", invalid_hexs_testdata)
    def test_input_str_handler_with_invalid_input(self, input_string, capsys):
        new_hex = Hexs()
        with pytest.raises(ValueError):
            new_hex.input_str_handler(input_string)
        captured = capsys.readouterr()
        assert "Invalid input. Please enter a valid hexadecimal number." in captured.out
        assert new_hex.dec_num is None
        assert new_hex.hex_num is None

    @pytest.mark.parametrize("input_string, expected_dec_num", hexs_testdata)
    def test_hex_to_dec_with_valid_input(self, input_string, expected_dec_num):
        new_hex = Hexs()
        assert new_hex.hex_to_dec(input_string) == expected_dec_num

    @pytest.mark.parametrize("input_string", invalid_hexs_testdata)
    def test_hex_to_dec_with_invalid_input(self, input_string):
        new_hex = Hexs()
        with pytest.raises(ValueError):
            new_hex.hex_to_dec(input_string)

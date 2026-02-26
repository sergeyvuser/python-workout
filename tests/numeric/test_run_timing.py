import pytest
from python_workout_pkg.numeric.run_timing import Run
from python_workout_pkg.utils.cli import CLI
from io import StringIO

# Parameterized data: (input, number_of_runs, result)
runs_testdata = [
    ("1\nquit\n", 1, 1.0),
    ("0\n1\nquit\n", 1, 1.0),
    ("10\n15\nquit\n", 2, 12.5),
    ("10.0\n12.0\n11\nquit\n", 3, 11.0),
    ("abc\n5\nquit\n", 1, 5.0),
    ("\n8\nquit\n", 1, 8.0),
]


class TestRuns:
    @pytest.mark.parametrize("runs_input, number_of_runs, result", runs_testdata)
    def test_run_timing_with_runs(
        self, monkeypatch, capsys, runs_input, number_of_runs, result
    ):
        """Parameterized test: different input scenarios"""
        monkeypatch.setattr("sys.stdin", StringIO(runs_input))
        run = Run()
        session = CLI(session_object=run)
        session.run_input_session()
        run.print_results()
        captured = capsys.readouterr()
        assert (
            f"Session ended\nAverage of {result}, over {number_of_runs} runs"
            in captured.out
        )
        assert captured.err == ""
        assert run.number_of_runs == number_of_runs
        assert run.total_time == result * number_of_runs
        assert run.average_time == result

    def test_end_session_no_runs(self, monkeypatch, capsys):
        """Test end session without runs"""
        monkeypatch.setattr("sys.stdin", StringIO("quit\n"))
        run = Run()
        session = CLI(session_object=run)
        session.run_input_session()
        captured = capsys.readouterr()
        assert "Session ended" in captured.out
        assert captured.err == ""
        assert run.number_of_runs == 0
        assert run.total_time == 0
        assert run.average_time == 0

    def test_run_timing_zero_input(self, capsys):
        """Test run timing with zero input"""
        run = Run()
        run.input_str_handler("0")
        captured = capsys.readouterr()
        assert "Too fast dude! Try again!" in captured.out
        assert captured.err == ""
        assert run.number_of_runs == 0

    def test_input_str_handler_invalid_input(self, capsys):
        """Test input str handler with invalid input raises ValueError"""
        run = Run()
        with pytest.raises(ValueError):
            run.input_str_handler("abc")
        captured = capsys.readouterr()
        assert "Hey! That's not a valid number!" in captured.out

    def test_run_timing_negative_input(self, capsys):
        """Test run timing with zero input"""
        run = Run()
        run.input_str_handler("-5")
        captured = capsys.readouterr()
        assert "Hey! You can run back in time?" in captured.out
        assert captured.err == ""
        assert run.number_of_runs == 0

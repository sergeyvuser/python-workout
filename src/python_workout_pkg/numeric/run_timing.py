from pydantic import BaseModel, computed_field
from python_workout_pkg.utils.cli import CLI


class Run(BaseModel):
    """
    Tracks 10 km run times and calculates average.

    Attributes:
        last_run_time: Time of the last run in minutes (None if no runs recorded).
        number_of_runs: Total number of runs recorded.
        total_time: Sum of all run times in minutes.
        average_time: (Computed) Average run time.
    """

    last_run_time: float | None = None
    number_of_runs: int = 0
    total_time: float = 0

    @computed_field
    @property
    def average_time(self) -> float:
        """Calculate average run time."""
        if self.number_of_runs == 0:
            return 0.0
        return self.total_time / self.number_of_runs

    def input_str_handler(self, input_string: str) -> None:
        """
        Process a single run time input.

        Args:
            input_string: The run time as a string.
        Raises:
            ValueError: If the input cannot be converted to a float.
        """
        if input_string == "0":
            print("Too fast dude! Try again!")
            return

        try:
            run_time = float(input_string)
        except ValueError as e:
            print("Hey! That's not a valid number!")
            raise e

        if run_time < 0:
            print("Hey! You can run back in time?")
            return

        self.last_run_time = run_time
        self.number_of_runs += 1
        self.total_time += self.last_run_time

    def print_results(self) -> None:
        """Print session end message with the average run time and the number of runs."""
        if self.number_of_runs == 0:
            print("No runs recorded.")
            return
        print(f"Average of {self.average_time}, over {self.number_of_runs} runs")


if __name__ == "__main__":
    run = Run()
    session = CLI(
        session_object=run,
        session_object_input_prompt="Enter 10 km run time: ",
        session_description="To add a run time, enter a number (positive float or int)\n",
    )
    session.run_input_session()
    run.print_results()

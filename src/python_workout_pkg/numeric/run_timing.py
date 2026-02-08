class Runs:
    """
    Calculates the average time of each run
    """

    def __init__(
        self, number_of_runs: int = 0, total_time: int = 0, average_time: float = 0
    ):
        """
        Initialises the Runs class
        Args:
            number_of_runs: the number of runs
            total_time: the total time
            average_time: the average time
        """
        self.number_of_runs = number_of_runs
        self.total_time = total_time
        self.average_time = average_time

    def run_timing(self):
        while True:
            try:
                one_run = float(input("Enter 10 km run time: "))
                if not one_run:
                    break
                self.number_of_runs += 1
                self.total_time += one_run
            except ValueError:
                print("Hey! That's not a valid number!")
            except TypeError:
                print("Hey! That's not a valid number!")
        try:
            self.average_time = self.total_time / self.number_of_runs
            print(f"Average of {self.average_time}, over {self.number_of_runs} runs")
        except ZeroDivisionError:
            print("No one run was added!")


if __name__ == "__main__":
    run = Runs()
    run.run_timing()

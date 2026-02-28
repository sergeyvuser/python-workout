import re

from python_workout_pkg.utils.cli import CLI
from pydantic import BaseModel


class Name(BaseModel):
    name: str | None = None

    def input_str_handler(self, input_string: str) -> None:
        """
        Handles the input string and calls name_triangle method to print a triangle of your name and a greeting message.

        Args:
            input_string: The input string to be handled.

        Returns:
            None

        Raises:
            ValueError: If the input string is not a valid name.
        """
        try:
            self.print_name_triangle(input_string)
        except ValueError as e:
            print("Invalid input. Please enter a valid name.")
            raise e

    def print_name_triangle(self, input_string: str) -> None:
        """
        Prints a triangle of your name and a greeting message.
        """
        input_string = re.sub(r"\s+", " ", input_string).strip()
        if not input_string:
            raise ValueError("Invalid input. Please enter a valid name.")

        self.name = input_string
        for i in range(len(self.name)):
            print(self.name[: i + 1])

        print(f"Hello, {self.name}!")


if __name__ == "__main__":
    new_name = Name()
    name_session = CLI(
        session_object=new_name,
        session_object_input_prompt="Enter your name: ",
        session_description="To print a triangle of your name, enter your name\n",
    )
    name_session.run_input_session()

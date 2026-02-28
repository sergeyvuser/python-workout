from python_workout_pkg.utils.cli import CLI
from pydantic import BaseModel


class Hexs(BaseModel):
    hex_num: str | None = None
    dec_num: int | None = None

    def input_str_handler(self, input_string: str) -> None:
        """
        Handles the input string and calls the hex_to_dec method.

        Args:
            input_string: The input string to be handled.

        Returns:
            None

        Raises:
            ValueError: If the input string is not a valid hexadecimal number.
        """
        try:
            self.ord_hex_to_dec(input_string)
        except ValueError as e:
            print("Invalid input. Please enter a valid hexadecimal number.")
            raise e

        self.hex_num = input_string
        self.print_results()

    def hex_to_dec(self, input_string: str) -> int | None:
        """
        Converts a hexadecimal number to decimal.

        Args:
            input_string: The hexadecimal number to convert.

        Returns:
            int | None: The decimal number or None if the input is invalid.

        Raises:
            ValueError: If the input string is not a valid hexadecimal number.
        """
        if input_string == "" or input_string is None:
            raise ValueError("Invalid input. Please enter a valid hexadecimal number.")

        self.dec_num = 0
        for power, digit in enumerate(input_string[::-1]):
            if digit.lower() in "0123456789abcdef":
                self.dec_num += int(digit, 16) * (16**power)
            else:
                self.dec_num = None
                raise ValueError(
                    "Invalid input. Please enter a valid hexadecimal number."
                )

        return self.dec_num

    def ord_hex_to_dec(self, input_string: str) -> int | None:
        if input_string == "" or input_string is None:
            raise ValueError("Invalid input. Please enter a valid hexadecimal number.")

        self.dec_num = 0
        for power, digit in enumerate(reversed(input_string)):
            if digit.lower() in "0123456789abcdef":
                dec_digit = ord(digit.lower())
                if 48 <= dec_digit <= 57:
                    dec_digit = dec_digit - 48
                else:
                    dec_digit = dec_digit - 87
                self.dec_num += dec_digit * (16**power)
            else:
                self.dec_num = None
                raise ValueError(
                    "Invalid input. Please enter a valid hexadecimal number."
                )

        return self.dec_num

    def print_results(self) -> None:
        """
        Prints the decimal number for a valid hexadecimal number or a message if no hexadecimal number was entered.
        """
        if self.hex_num is not None:
            print(f"Decimal number: {self.dec_num}")
        else:
            print("No hexadecimal number entered.")


if __name__ == "__main__":
    new_hex = Hexs()
    session = CLI(
        session_object=new_hex,
        session_object_input_prompt="Enter a hexadecimal number to convert to decimal: ",
        session_description="To convert a hexadecimal number to decimal, enter a hexadecimal number\n",
    )
    session.run_input_session()

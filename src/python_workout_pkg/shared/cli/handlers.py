from pydantic import BaseModel, ValidationError
from typing import Type, TypeVar, Callable


class CLI(BaseModel):
    """
    CLI class for handling command line input.

    Attributes:
        session_object: The session object to use.
        session_object_input_prompt: The input prompt for the session object.
        session_description: The description of the session to be displayed.
    """

    session_object: object
    session_object_input_prompt: str = "Enter session input: "
    session_description: str | None = None

    def run_input_session(self) -> None:
        """
        Run the interactive session.
        It handles input strings and calls the input_str_handler method of the session object.
        """
        print("Session started. To end session, enter 'quit'")
        if self.session_description:
            print(self.session_description)

        while True:
            input_str = input(self.session_object_input_prompt)
            if input_str == "quit":
                print("Session ended")
                break
            try:
                self.session_object.__getattribute__("input_str_handler")(input_str)
            except ValueError:
                continue
            except AttributeError:
                print(
                    "AttributeError: Your session object has no attribute 'input_str_handler' to handle input strings.\n"
                    "Please define it for your class object."
                )
                break


T = TypeVar("T", bound=BaseModel)


class CLIInputHandler:
    """
    CLIInputHandler class for handling command line input.
    """

    def __init__(
        self,
        model: Type[T],
        collector: Callable[[], dict] | None,
        formatter: Callable[[T], str] | None = None,
        quit_commands: tuple = ("quit", "exit", "q"),
        session_description: str | None = None,
    ) -> None:
        self.model = model
        self.collector = collector
        self.formatter = formatter or (lambda instance: str(instance))
        self.quit_commands = quit_commands
        self.session_description = session_description

    def run_input_session(self) -> list[T]:
        """
        Run the interactive session.
        It handles input strings and calls the input_str_handler method of the session object.
        Returns:
            list[T]: List of validated models
        """
        print(
            f"Session started.\nTo end session, enter any of the command {self.quit_commands}"
        )
        if self.session_description:
            print(self.session_description)

        results = []

        while True:
            raw = self.collector()

            # quit если collector вернул сигнал выхода
            if raw is None:
                print("Session finished. Quit.")
                break

            try:
                instance = self.model(**raw)
                results.append(instance)
                print(self.formatter(instance))
            except ValidationError as e:
                for err in e.errors():
                    print(err["msg"])

        return results

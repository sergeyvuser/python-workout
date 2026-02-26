from pydantic import BaseModel


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
        print("To end session, enter 'quit'")
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

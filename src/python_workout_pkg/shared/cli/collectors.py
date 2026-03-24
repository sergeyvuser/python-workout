from typing import Callable


def collect_input(
    prompt: str = "Enter input: ",
    quit_commands: tuple = ("q", "quit", "exit"),
    transformer: Callable[[str], dict] | None = None,
) -> dict | None:
    """
    Collects user input and returns it as a dictionary.
        Attributes:
            prompt (str): The prompt to display to the user.
            quit_commands (tuple): Commands to quit the input session.
            transformer (Callable[[str], dict] | None): Optional transformer to apply to the input and return a transformed dictionary.
        Returns:
            dict | None: The collected input as a dictionary or None if the input is in quit_commands.
    """
    raw = input(f"\n{prompt}").strip()

    if raw.lower() in quit_commands:
        return None

    if transformer:
        return transformer(raw)

    return {"value": raw}


def collect_user_input() -> dict | None:
    """
    Example for models: Collects user input for name and age.
    """
    name = collect_input(prompt="Введите имя")
    if name is None:
        return None

    age = collect_input(prompt="Введите возраст")
    if age is None:
        return None

    return {"name": name["value"], "age": age["value"]}

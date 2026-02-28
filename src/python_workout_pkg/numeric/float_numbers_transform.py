def transform_float_numbers(
    float_number: float, before_dot: int, after_dot: int
) -> float | None:
    """
    Transform float number to string and cut it to before_dot and after_dot

    Args:
        float_number (float): float number
        before_dot (int): digits before point
        after_dot (int): digits after point
    Returns:
        float_number (float): transformed float number
    """
    try:
        str_number = str(float(float_number))
        point_index = str_number.index(".")
        if before_dot < 0 and after_dot < 0:
            return float_number
        elif before_dot < 0 or before_dot > point_index:
            return float(str_number[: point_index + after_dot + 1])
        elif after_dot < 0:
            return float(str_number[point_index - before_dot :])
        return float(str_number[point_index - before_dot : point_index + after_dot + 1])

    except TypeError as e:
        print("There is an error: ", e, "\nCheck your arguments")
    except ValueError as e:
        print("There is an error: ", e, "\nCheck your arguments")


if __name__ == "__main__":
    print(transform_float_numbers(0.2323, 1, 100))

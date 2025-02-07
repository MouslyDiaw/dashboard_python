""" Calculator module."""


def calculate(operation: str, x: float, y: float):
    """Compute arithmetic operation.

    Args:
        operation: name of operation to manage
            Possible values are: ("Addition", "Subtraction", "Multiplication", "Division")
        x: input value
        y: input value

    Returns:
        float
        if "Addition", we return x + y
        if "Subtraction", we return x - y
        if "Multiplication", we return x * y
        if "Division":
            if y != 0, we return x / y
            else, we return a message

    """
    valid_operations = ("Addition", "Subtraction", "Multiplication", "Division")
    if operation not in valid_operations:
        return f"operation must be in {valid_operations}, but you gave {operation}"
    elif operation == "Addition":
        return x + y
    elif operation == "Subtraction":
        return x - y
    elif operation == "Division":
        if not y:
            return f"You must be defined a value different to zero for y"
        return x / y
    return x * y

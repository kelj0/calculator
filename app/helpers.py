import typing as tp

def load_operators_from_database() -> tp.List:
    """
    Connects to the database and fetches available operands
    """
    # connect to database, fetch available operators..
    return ["+", "-", "*", "/"]

def do_calculation(first_number, second_number, operator) -> tp.Union[tp.AnyStr, float]:
    """
    Returns result from calculation using
    - **first_number**
    - **second_number**
    - **operator**
    """
    operators = load_operators_from_database()
    if operator not in operators:
        return "Operand not supported"
    first_number = float(first_number)
    second_number = float(second_number)
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        if second_number == 0:
            return "You cannot divide by zero."
        return first_number / second_number

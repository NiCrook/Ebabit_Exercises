#   https://edabit.com/challenge/WKJwo2xDNjKxwtGoH
#   Write two functions:
#   1. to_int(): A function to convert a string to an intereger
#   2. to_str(): A function to convert an integer to a string


def to_int(string_input: str) -> int:
    try:
        number = int(string_input)
        return number
    except ValueError as err:
        print(f"Error: {err}")


def to_str(number: int) -> str:
    try:
        string = str(number)
        return string
    except ValueError as err:
        print(f"Error: {err}")


print(to_int("77"))
print(to_str(77))

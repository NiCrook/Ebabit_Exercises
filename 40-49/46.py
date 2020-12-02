#   https://edabit.com/challenge/HYjQKDXFfeppcWmLX
#   In this challenge, establish if a given integer num is a Curzon number.
#   If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
#   Given a non-negative integer num
#   implement a function that returns True if num is a Curzon number, or False otherwise.


def is_curzon(num1: int) -> bool:
    try:
        first_result = (2 ** num1) + 1
        second_result = (2 * num1) + 1
        remainder = first_result % second_result
        if remainder:
            return False
        return True
    except TypeError as err:
        print(f"Error: {err}")


print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))

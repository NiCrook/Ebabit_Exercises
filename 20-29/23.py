#   https://edabit.com/challenge/Rx2pkSA9dCmtwS8xt
#   Create a function that takes a number as its only argument
#   returns True if it's less than or equal to zero, otherwise return False


def zero_or_less(number: int) -> bool:
    try:
        if number <= 0:
            return True
        elif number > 0:
            return False
    except ValueError as err:
        print(f"Error: {err}")


print(zero_or_less(5))
print(zero_or_less(1))
print(zero_or_less(-3))
print(zero_or_less(0))

#   https://edabit.com/challenge/49pyDP8dE3pJ2dYMW
#   Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.


def divisible_by_five(num1: int) -> bool:
    try:
        if (num1 % 5) == 0:
            return True
        else:
            return False
    except ValueError as err:
        print(f"Error: {err}")


print(divisible_by_five(5))
print(divisible_by_five(-55))
print(divisible_by_five(37))

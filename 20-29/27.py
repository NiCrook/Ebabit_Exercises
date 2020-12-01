#   https://edabit.com/challenge/pZ3HxBfvejsvkEDo4
#   Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.


def less_than_one_hundred(num1: int, num2: int) -> bool:
    try:
        result = num1 + num2
        if result < 100:
            return True
        else:
            return False
    except ValueError as err:
        print(f"Error: {err}")


print(less_than_one_hundred(22, 15))
print(less_than_one_hundred(83, 34))
print(less_than_one_hundred(3, 77))

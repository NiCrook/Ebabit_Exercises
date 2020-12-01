#   https://edabit.com/challenge/NRxWszQRw5JqSDmQS
#   Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.


def divides_evenly(num1: int, num2: int) -> bool:
    try:
        result = num1 / num2
        if result % 2 == 0:
            return True
        else:
            return False
    except TypeError as err:
        print(f"Error: {err}")


print(divides_evenly(98, 7))
print(divides_evenly(85, 4))

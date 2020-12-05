#   https://edabit.com/challenge/2bTdN8sr3PQKkLHur
#   You are given two numbers a and b.
#   Create a function that returns the next number greater than a and b and divisible by b.
#   a will always be greater than b.


def divible_by_b(a: int, b: int) -> int:
    try:
        c = a + 1
        while c % b != 0:
            c += 1
        else:
            return c
    except TypeError as err:
        print(f"Error: {err}")


print(divible_by_b(17, 8))
print(divible_by_b(98, 3))
print(divible_by_b(14, 11))

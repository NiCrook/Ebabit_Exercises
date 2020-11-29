#   https://edabit.com/challenge/KWoj7kWiHRqJtG6S2
#   There is a single operator in Python
#   capable of providing the remainder of a division operation.
#   Two numbers are passed as parameters.
#   The first parameter divided by the second parameter will have a remainder, possibly zero.
#   Return that value.


def remainder(int1: int, int2: int) -> int:
    leftovers = int1 % int2
    return leftovers


print(remainder(5, 5))

#   https://edabit.com/challenge/D2Hvq6NZchp7Q6ftR
#   Create a function which returns the Modulo of the two given numbers.


def mod(int1: int, int2: int) -> int:
    leftovers = int1 % int2
    return leftovers


print(mod(-13, 64))

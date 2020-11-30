#   https://edabit.com/challenge/xWSjvoH7mEkSnqS7H
#   Create a function that takes a base number and an exponent number and returns the calculation.


def power_of(base: int, power: int) -> int:
    tracker = power
    while tracker != 1:
        base = base * power
        tracker -= 1
    return base


print(power_of(5, 5))

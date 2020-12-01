#   https://edabit.com/challenge/gbWDtMHtZARm7sdNA
#   Python has a logical operator "and".
#   The "and" operator takes two boolean values, and returns True if both values are True.


def and_(bool1: bool, bool2: bool) -> bool:
    try:
        if bool1 and bool2:
            return True
        else:
            return False
    except TypeError as err:
        print(f"Error: {err}")


print(and_(True, False))
print(and_(True, True))
print(and_(False, False))
print(and_(False, True))

#   https://edabit.com/challenge/QKmETue6fMTdcB8Rq
#   Create a recursive function that takes two
#   and repeats the string n number of times.
#   The first parameter txt is the string to be repeated
#   and the second parameter is the number of times the string is to be repeated.


def repition(user_str: str, num1: int) -> str:
    result = user_str * num1
    return result


print(repition("ab", 3))
print(repition("kiwi", 1))
print(repition("cherry", 2))

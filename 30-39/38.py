#   https://edabit.com/challenge/C3N2JEfFQoh4cqQ98
#   Create a function that takes two strings as
#   and return either True or False
#   depending on whether the total number of characters in the first string
#   is equal to the total number of characters in the second string.


def comp(str1: str, str2: str) -> bool:
    try:
        if len(str1) == len(str2):
            return True
        else:
            return False
    except TypeError as err:
        print(f"Error: {err}")


print(comp("ab", "cd"))
print(comp("abc", "de"))
print(comp("hello", "edabit"))

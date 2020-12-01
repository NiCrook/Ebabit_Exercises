#   https://edabit.com/challenge/wtu32ZFxHJsuQnogX
#   Create a function that returns True if a string is empty and False otherwise.


def is_empty(str1: str) -> bool:
    try:
        if len(str1) == 0:
            return True
        else:
            return False
    except TypeError as err:
        print(f"Error: {err}")


print(is_empty(""))
print(is_empty(" "))
print(is_empty("hi"))

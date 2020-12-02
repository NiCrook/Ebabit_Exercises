#   https://edabit.com/challenge/JCZqhijycsNizczsR
#   Given two arguments, return a list which contains these two arguments.


def make_pair(arg1: str or int or bool, arg2: str or int or bool) -> list:
    try:
        result = []
        result.append(arg1)
        result.append(arg2)
        return result
    except TypeError as err:
        print(f"Error: {err}")


print(make_pair(1, 2))
print(make_pair(51, 21))
print(make_pair(512124, 215))

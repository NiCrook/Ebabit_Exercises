#   https://edabit.com/challenge/CjXamaNRmKxwkmBxq
#   define a function that takes a number and finds the cube and returns the cube


def cube(number: int) -> int:
    cube = (number * number) * number
    return cube


print(cube(5))

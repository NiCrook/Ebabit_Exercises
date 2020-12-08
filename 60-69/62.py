#   https://edabit.com/challenge/nn7JKRBfq8iDcX8ZB
#   Write a function that returns a lambda expression
#   which transforms its input by adding a particular suffix at the end.


def add_suffix(suffix):
    return lambda word: word + suffix


add_ly = add_suffix("ly")
print(add_ly("hopeless"))
print(add_ly("total"))

add_less = add_suffix("less")
print(add_less("fear"))
print(add_less("ruth"))

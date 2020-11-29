#   https://edabit.com/challenge/aWLTzrRsrw7RakYrN
#   Write a function that takes the base and height of a triangle and return its area.
#   area = (base * height) / 2


def area_finder(base: float, height: float) -> float:
    area = (base * height) / 2
    return area


print(area_finder(10.0, 10.0))

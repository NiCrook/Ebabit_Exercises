#   https://edabit.com/challenge/Yx2a9B57vXRuPevGh
#   Create a function that takes length and width and finds the perimeter of a rectangle.


def find_perimeter(x: int, y: int) -> int:
    perimeter = (x * 2) + (y * 2)
    return perimeter


print(find_perimeter(20, 10))

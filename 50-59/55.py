#   https://edabit.com/challenge/NNhkGocuPMcryW7GP
#   Imagine a circle and two squares: a smaller and a bigger one.
#   For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.
#   Create a function, that takes an integer (radius of the circle)
#   returns the difference of the areas of the two squares.


def area_difference(radius: int) -> int:
    try:
        diameter = radius * 2
        big_area = diameter * diameter
        little_square = big_area / 2
        difference = big_area - little_square
        return int(difference)
    except TypeError as err:
        print(f"Error: {err}")


print(area_difference(5))
print(area_difference(6))
print(area_difference(7))

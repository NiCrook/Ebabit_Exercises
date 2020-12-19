# https://edabit.com/challenge/662nTYb83Lg3oNN79
#
# Given a list of four points in the plane, determine if they are the vertices of a parallelogram.
# Examples
#
# is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True
#
# is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False
#
# is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True
#
# is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True
#
# is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True
#
# Notes
#
# The points may be given in any order (compare examples #1 and #5).


def is_parallelogram(four: list):
    slopes = []
    two_coords = []
    a, b = 0, 1

    def find_slope(x1, x2, y1, y2):
        try:
            slope = (y2 - y1) / (x2 - x1)
            return slope
        except ZeroDivisionError:
            slope = 0
            return slope

    while len(slopes) != len(four):
        if b != len(four):
            x1 = four[a][0]
            x2 = four[b][0]
            y1 = four[a][1]
            y2 = four[b][1]
            slope = find_slope(x1, x2, y1, y2)
            slopes.append(slope)
            a += 1
            b += 1
        else:
            x1 = four[-1][0]
            x2 = four[0][0]
            y1 = four[-1][1]
            y2 = four[0][1]
            slope = find_slope(x1, x2, y1, y2)
            slopes.append(slope)

    if slopes[0] == slopes[2] or slopes[0] == (slopes[2] * -1):
        if slopes[1] == slopes[3] or slopes[1] == (slopes[3] * -1):
            return True
        else:
            return False


print(is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]))
print(is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]))
print(is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]))
print(is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]))
print(is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]))
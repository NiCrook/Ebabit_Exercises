# https://edabit.com/challenge/76ibd8jZxvhAwDskb
#
# A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of
# the tallest building is 4 (second-most right column).
#
# [[0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 1, 1]]
#
# Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
# Examples
#
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 3
#
# tallest_skyscraper([
#   [0, 1, 0, 0],
#   [0, 1, 0, 0],
#   [0, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 4
#
# tallest_skyscraper([
#   [0, 0, 0, 0],
#   [0, 0, 0, 0],
#   [1, 1, 1, 0],
#   [1, 1, 1, 1]
# ]) ➞ 2


def tallest_skyscraper(skyline: list) -> int:
    #   assign placeholder variables
    cur_ind = 0
    cur_nestdex = 0
    tallest = 0
    height_lst = []

    #   fill height list to the len of a nested list in skyline, values set as placeholders
    while len(height_lst) != len(skyline[0]):
        height_lst.append(0)

    #   check if element in nested list is 1, if so, +1 to the corresponding element in height list
    while cur_ind != len(skyline):
        while cur_nestdex != len(skyline[0]):
            if skyline[cur_ind][cur_nestdex] == 1:
                height_lst[cur_nestdex] += 1
            cur_nestdex += 1
        cur_ind += 1
        cur_nestdex = 0

    #   check for tallest tower
    while len(height_lst) != 0:
        if height_lst[0] > tallest:
            tallest = height_lst[0]
            del height_lst[0]
        else:
            del height_lst[0]

    return tallest


print(tallest_skyscraper([
  [0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 1, 1, 0, 0],
  [1, 1, 1, 1, 0]
]))

print(tallest_skyscraper([
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]))

#   https://edabit.com/challenge/G9QRtAGXb9Cu368Pw
#   Create a function that takes a variable number of arguments
#   each argument representing the number of items in a group
#   and returns the number of permutations (combinations) of items that you could get
#   by taking one item from each group.


def combinations(*args: int) -> int:
    combo_list = []
    for arg in args:
        combo_list.append(arg)
    while len(combo_list) != 1:
        combo_list[0] = combo_list[0] * combo_list[1]
        del combo_list[1]
    return combo_list[0]


print(combinations(2, 3))
print(combinations(3, 7, 4))
print(combinations(2, 3, 4, 5))

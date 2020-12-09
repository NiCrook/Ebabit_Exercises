#   https://edabit.com/challenge/qbCavpBpk8KSWM37s
#   Given a list of integers, return the largest gap between elements of the sorted version of that list.


def largest_gap(user_list: list) -> int:
    user_list.sort()
    current_gap = 0
    while len(user_list) != 1:
        gap = user_list[1] - user_list[0]
        if gap > current_gap:
            current_gap = gap
        del user_list[0]
    return current_gap


print(largest_gap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]))
print(largest_gap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]))
print(largest_gap([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]))

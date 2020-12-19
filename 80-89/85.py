# https://edabit.com/challenge/4wJc7maZhYCSgzyRS
#
# Create a function that takes a list lst and a number N and returns a list of two integers from lst whose product is
# that of the number N. Examples
#
# two_product([1, 2, -1, 4, 5], 20) ➞ [4, 5]
#
# two_product([1, 2, 3, 4, 5], 10) ➞ [2, 5]
#
# two_product([100, 12, 4, 1, 2], 15) ➞ None
#
# Note:
#
#     Try doing this with 0(N) time complexity.
#     No duplicates.
#     In the list there can be multiple solutions so return the first full match that you have found.
#     If any doubts please refer to the comments section.


def two_product(lst: list, n: int) -> list:
    first_ind = 0
    sec_ind = 1
    product_list = []

    while first_ind != len(lst):
        while sec_ind != len(lst):
            if lst[first_ind] * lst[sec_ind] == n:
                product_list.append(lst[first_ind])
                product_list.append(lst[sec_ind])
                return product_list
            else:
                sec_ind += 1
        first_ind += 1
        sec_ind = first_ind + 1


print(two_product([1, 2, -1, 4, 5], 20))
print(two_product([1, 2, 3, 4, 5], 10))
print(two_product([100, 12, 4, 1, 2], 15))

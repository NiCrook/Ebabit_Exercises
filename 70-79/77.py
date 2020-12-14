# https://edabit.com/challenge/KLke67efuam6ajLrt
#
# An out-shuffle, also known as an out faro shuffle or a perfect shuffle, is a controlled method for shuffling
# playing cards. It is performed by splitting the deck into two equal halves and interleaving them together
# perfectly, with the condition that the top card of the deck remains in place.
#
# Using an array to represent a deck of cards, an out-shuffle looks like:
#
# [1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
# // Card 1 remains in the first position.
#
# If we repeat the process, the deck eventually returns to original order.
#
# Shuffle 1:
#
# [1, 2, 3, 4, 5, 6, 7, 8] ➞ [1, 5, 2, 6, 3, 7, 4, 8]
#
# Shuffle 2:
#
# [1, 5, 2, 6, 3, 7, 4, 8] ➞ [1, 3, 5, 7, 2, 4, 6, 8]
#
# Shuffle 3:
#
# [1, 3, 5, 7, 2, 4, 6, 8] ➞ [1, 2, 3, 4, 5, 6, 7, 8]
# // Back where we started.
#
# Write a function that takes a positive even integer representing the number of the cards in a deck, and returns the
# number of out-shuffles required to return the deck to its original order. Examples
#
# shuffle_count(8) ➞ 3
#
# shuffle_count(14) ➞ 12
#
# shuffle_count(52) ➞ 8
#
# Notes
#
#     The number of cards is always even and greater than one. Thus, the smallest possible deck size is two.
#     A recursive version of this challenge can be found in here.


def shuffle_count(cards: int):
    if cards % 2 != 0:
        print("\nValue must be an even integer.")
    half = int(cards / 2)
    cur_val = 1
    cur_ind = 0
    lst1 = []
    lst2 = []
    shuffled_list = []

    while len(lst2) != half:
        lst2.append(cur_val + 1)
        cur_ind += 1
        cur_val += 2

    cur_val = 1
    cur_ind = 0

    while len(lst1) != half:
        lst1.append(cur_val)
        cur_ind += 1
        cur_val += 2

    while len(shuffled_list) != cards:
        shuffled_list.append(lst1[0])
        shuffled_list.append(lst2[0])
        del lst1[0]
        del lst2[0]

    return shuffled_list


print(shuffle_count(8))
print(shuffle_count(14))
print(shuffle_count(52))

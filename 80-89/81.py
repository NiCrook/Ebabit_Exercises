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


def shuffle_count(cards: int):
    shuffles = 0
    original_deck = list(range(0, cards))
    first_half = []
    second_half = []
    shuffled_deck = []

    def half(half_, deck_, cur_ind):
        half = int(cards / 2)
        while len(half_) != half:
            half_.append(deck_[cur_ind])
            original_deck[cur_ind] = half_[cur_ind]
            cur_ind += 1

    half(first_half, original_deck, 0)
    half(second_half, original_deck, int(cards / 2))
    shuffles += 1

    while len(shuffled_deck) != cards:
        shuffled_deck.append(first_half[0])
        shuffled_deck.append(second_half[0])
        del first_half[0], second_half[0]

    while shuffled_deck != original_deck:
        shuffles += 1

        half(first_half, shuffled_deck, 0)
        half(second_half, shuffled_deck, int(cards / 2))

        shuffled_deck = []

        while len(shuffled_deck) != len(original_deck):
            shuffled_deck.append(first_half[0])
            shuffled_deck.append(second_half[0])
            del first_half[0], second_half[0]

    return shuffles


print(shuffle_count(8))
print(shuffle_count(14))
print(shuffle_count(52))

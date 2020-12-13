# https://edabit.com/challenge/LR98GCwLGYPSv8Afb
#
# Given a list of words in the singular form, return a set of those words in the plural form if they appear more than
# once in the list. Examples
#
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
#
# pluralize(["table", "table", "table"]) ➞ { "tables" }
#
# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
#
# Notes
#
#     This is an oversimplification of the English language so no edge cases will appear.
#     Only focus on whether or not to add an s to the ends of words.
#     All tests will be valid.


def pluralize(word_list: list):
    cur_ind = 0
    lst_len = len(word_list)
    word_set = set()
    word_dict = {}

    while cur_ind != lst_len:
        if word_list[cur_ind] not in word_dict:
            word_dict[word_list[cur_ind]] = 1
            cur_ind += 1
        else:
            word_dict[word_list[cur_ind]] += 1
            cur_ind += 1

    for word in word_dict:
        if word_dict[word] > 1:
            word = f"{word}s"
            word_set.add(word)
        else:
            word_set.add(word)

    return word_set


print(pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))

#   https://edabit.com/challenge/jwzgYjymYK7Gmro93
#   Create a function that returns the indices of all occurrences of an item in the list.


def get_indices(user_list: list, item: str or int) -> list:
    current_indice = 0
    occurence_list = []
    while len(user_list):
        if user_list[0] == item:
            occurence_list.append(current_indice)
            current_indice += 1
        else:
            current_indice += 1
        del user_list[0]
    return occurence_list


print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
print(get_indices([1, 5, 5, 2, 7], 7))
print(get_indices([1, 5, 5, 2, 7], 5))
print(get_indices([1, 5, 5, 2, 7], 8))

#   https://edabit.com/challenge/cCWMeiJCP9Ef8XMq8
#   Create a function to concatenate two integer lists.


def concat(list1: list, list2: list) -> list:
    try:
        concated_list = list1 + list2
        return concated_list
    except TypeError as err:
        print(f"Error: {err}")


print(concat([1, 3, 5], [2, 6, 8]))
print(concat([7, 8], [10, 9, 1, 1, 2]))
print(concat([4, 5, 1], [3, 3, 3, 3, 3]))

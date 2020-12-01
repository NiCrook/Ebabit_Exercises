#   https://edabit.com/challenge/uPtuNNTuASzPZMQrW
#   Create a function that accepts a list and returns the last item in the list.
#   The list can be either homogeneous or heterogeneous.


def get_last_item(user_list: list) -> int or float or str or bool:
    try:
        last_index = user_list[-1]
        return last_index
    except TypeError as err:
        print(f"Error: {err}")


print(get_last_item([1, 2, 3]))
print(get_last_item(["cat", "dog", "duck"]))
print(get_last_item([True, False, True]))
print(get_last_item([7, "String", False]))
print(get_last_item(1))

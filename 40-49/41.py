#   https://edabit.com/challenge/HRu9WggWxdSpYjxNf
#   Given a list of numbers
#   return True if the sum of the values in the list is less than 100;
#   otherwise return False.


def list_less_then_hunnid(user_list: list) -> bool:
    try:
        result = 0
        while len(user_list):
            result += user_list[0]
            del user_list[0]
        if result < 100:
            return True
        else:
            return False
    except TypeError as err:
        print(f"Error: {err}")


print(list_less_then_hunnid([5, 57]))
print(list_less_then_hunnid([77, 30]))
print(list_less_then_hunnid([0]))

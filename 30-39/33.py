#   https://edabit.com/challenge/foFKdr68vSENQ9AYB
#   Create a function that takes a list and returns the sum of all numbers in the list.
from typing import List


def get_sum_of_elements(user_list: List[int]) -> int:
    try:
        sum_ = 0
        while len(user_list) != 0:
            sum_ += user_list[0]
            del user_list[0]
        return sum_
    except TypeError as err:
        print(f"Error: {err}")


print(get_sum_of_elements([2, 7, 4]))
print(get_sum_of_elements([45, 3, 0]))
print(get_sum_of_elements([-2, 84, 23]))
print(get_sum_of_elements(["hi", "hi"]))

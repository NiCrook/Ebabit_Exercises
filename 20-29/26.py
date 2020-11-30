#   https://edabit.com/challenge/6fx8iNCHETW8KqAui
#   Given a list of integers
#   return the difference between the largest and smallest integers in the list


def difference(number_list: list) -> int:
    number_list.sort()
    result = number_list[-1] - number_list[0]
    return result


print(difference([10, 15, 20, 2, 10, 6]))
print(difference([-3, 4, -9, -1, -2, 15]))
print(difference([4, 17, 12, 2, 10, 2]))

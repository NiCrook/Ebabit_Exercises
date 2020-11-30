#   https://edabit.com/challenge/ecSZ5kDBwCD3ctjE6
#   Create a function that takes a list of numbers and returns the smallest number in the list.


def smallest_number(number_list: list) -> float:
    while len(number_list) != 1:
        if number_list[0] > number_list[1]:
            del number_list[0]
        elif number_list[0] < number_list[1]:
            del number_list[1]
        elif number_list[0] == number_list[1]:
            del number_list[0]
    if len(number_list) == 1:
        return number_list[0]


print(smallest_number([34, 15, 88, 2]))
print(smallest_number([34, -345, -1, 100]))
print(smallest_number([-76, 1.345, 1, 0]))
print(smallest_number([0.4356, 0.8795, 0.5435, -0.9999]))
print(smallest_number([7, 7, 7]))

#   https://edabit.com/challenge/A7hyDnb72prWryeuY
#   Create a function that takes a list of numbers. Return the largest number in the list.


def largest_number(number_list: list) -> int:
    while len(number_list) != 1:
        if number_list[0] > number_list[1]:
            del number_list[1]
        elif number_list[0] < number_list[1]:
            del number_list[0]
        elif number_list[0] == number_list[1]:
            del number_list[0]
    if len(number_list) == 1:
        return number_list[0]


print(largest_number([4, 5, 1, 3]))
print(largest_number([300, 200, 600, 150]))
print(largest_number([1000, 1001, 857, 1]))

#   https://edabit.com/challenge/qaNmoG4dAXRL5JqvA
#   Create a function that takes a list containing nested lists as an argument.
#   Each sublist has 2 elements.
#   The first element is the numerator and the second element is the denominator.
#   Return the sum of the fractions rounded to the nearest whole number.


def sum_fractions(nested_list: list) -> int:
    total_sum = 0
    while len(nested_list) != 0:
        current_list = nested_list[0]
        while len(current_list) != 1:
            current_fraction = current_list[0] / current_list[1]
            total_sum = total_sum + current_fraction
            del current_list[0]
        del nested_list[0]
    return int(total_sum)


print(sum_fractions([[18, 13], [4, 5]]))
print(sum_fractions([[36, 4], [22, 60]]))
print(sum_fractions([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))

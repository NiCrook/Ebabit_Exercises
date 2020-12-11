#   https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
#   A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
#   Create a function that determines whether a number is a Disarium or not.


def is_disarium(num1: int):
    str_num = str(num1)
    num_len = len(str_num)
    cur_ind = num_len - 1
    raised_sum = 0

    num_list = []
    raise_list = []

    #   create list out of input number
    while len(str_num) != 0:
        num_list.append(str_num[0])
        str_num = str_num[1:]

    #   create list to find raised product
    while len(num_list) != 1:
        while num_len != 0:
            raise_list.append(num_list[cur_ind])
            num_len -= 1

        while len(raise_list) != 1:
            raise_list[0] = int(raise_list[0]) * int(raise_list[1])
            del raise_list[1]

        raised_sum += raise_list[0]
        del raise_list[0]
        del num_list[-1]
        num_len = len(num_list)
        cur_ind = num_len - 1

    raised_sum += int(num_list[0])
    if raised_sum == num1:
        return True
    elif raised_sum != num1:
        return False


print(is_disarium(7))
print(is_disarium(75))
print(is_disarium(135))
print(is_disarium(518))
print(is_disarium(8))

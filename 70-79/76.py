# https://edabit.com/challenge/jwzAdBnJnBxCe4AXP
#
# Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits
# are rearranged. Examples
#
# rearranged_difference(972882) ➞ 760833
# # 988722 - 227889 = 760833
#
# rearranged_difference(3320707) ➞ 7709823
# # 7733200 - 23377 = 7709823
#
# rearranged_difference(90010) ➞ 90981
# # 91000 - 19 = 90981


def rearranged_difference(scrambled_number: int) -> int:
    str_num = str(scrambled_number)
    ascending_num = ""
    descending_num = ""
    ascending_lst = []
    descending_lst = []

    for i in str_num:
        ascending_lst.append(i)
        descending_lst.append(i)
    ascending_lst.sort()
    descending_lst.sort(reverse=True)

    for i in ascending_lst:
        ascending_num += str(i)

    for i in descending_lst:
        descending_num += str(i)

    difference = int(descending_num) - int(ascending_num)
    return difference


print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))

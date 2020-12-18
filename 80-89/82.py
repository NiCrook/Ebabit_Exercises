# https://edabit.com/challenge/QN4RMpAnktNvMCWwg
#
# An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom
# right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of
# relativity.
#
# Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge,
# if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter
# if the mirror image is left-right or top-bottom. Examples
#
# id_mtrx(2) ➞ [
#   [1, 0],
#   [0, 1]
# ]
#
# id_mtrx(-2) ➞ [
#   [0, 1],
#   [1, 0]
# ]
#
# id_mtrx(0) ➞ []
#
# Notes
#
# Incompatible types passed as n should return the string "Error".


def id_mtrx(n: int):
    try:
        num_lsts = 0
        lists = []

        if n > 0:
            lst_ind = 0
            while num_lsts != n:
                lst = []
                while len(lst) != n:
                    lst.append(0)
                lst[lst_ind] = 1
                lists.append(lst)
                num_lsts += 1
                lst_ind += 1
        elif n < 0:
            lst_ind = -1
            while num_lsts != (n * -1):
                lst = []
                while len(lst) != (n * -1):
                    lst.append(0)
                lst[lst_ind] = 1
                lists.append(lst)
                num_lsts += 1
                lst_ind -= 1

        return lists
    except TypeError as err:
        return f"Error: {err}"


print(id_mtrx(2))
print(id_mtrx(-2))
print(id_mtrx(0))

# https://edabit.com/challenge/Fpymv2HieqEd7ptAq
#
# Write a function that groups a string into parentheses cluster. Each cluster should be balanced.
# Examples
#
# split("()()()") ➞ ["()", "()", "()"]
#
# split("((()))") ➞ ["((()))"]
#
# split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]
#
# split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]
#
# Notes
#
#     All input strings will only contain parentheses.
#     Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.

#   assign placeholder variables
#   turn string into list
#   check if len of string_list is equal to zero
#   if so
#   then check index a of list
#      if index a of list is "(", plus one to a and c
#      if index b of list is "(", plus one to b and c, if index b of list is ")", plus one to b and minus one from
#      add either to cur_sub
#      if c = -1, append cur_sub to lst, reset a to b + 1, reset b to a + 1, reset c to 0, clear cur_sub
#   if not
#   then return lst


def split(string):
    a, b = 0, 0
    cur_sub = ""
    lst = []
    str_lst = list(string)

    while len(str_lst) != 0:
        while cur_sub == "":
            if str_lst[0] == "(":
                cur_sub += "("
                a += 1
            else:
                if str_lst[0] == ")":
                    del str_lst[0]

        while b != -1:
            if str_lst[a] == "(":
                cur_sub += "("
                a += 1
                b += 1
            elif str_lst[a] == ")":
                cur_sub += ")"
                a += 1
                b -= 1

        if b == -1:
            lst.append(cur_sub)
            cur_sub = ""
            del str_lst[0:a]
            a, b = 0, 0

    return lst


print(split("()()()"))
print(split("((()))"))
print(split("((()))(())()()(()())"))
print(split("((())())(()(()()))"))
print(split(")()()()"))

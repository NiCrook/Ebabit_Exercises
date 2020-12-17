# https://edabit.com/challenge/SHdu4GwBQehhDm4xT
#
# A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked
# cell and a 0 represents a locked cell.
#
# [1, 1, 0, 0, 0, 1, 0]
#
# Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch.
# You are the prisoner in the first cell. If the first cell is locked, you cannot free anyone. Each time you free a
# prisoner, the locked cells become unlocked, and the unlocked cells become locked again.
#
# So, if we use the example above:
#
# [1, 1, 0, 0, 0, 1, 0]
# # You free the prisoner in the 1st cell.
#
# [0, 0, 1, 1, 1, 0, 1]
# # You free the prisoner in the 3rd cell (2nd one locked).
#
# [1, 1, 0, 0, 0, 1, 0]
# # You free the prisoner in the 6th cell (3rd, 4th and 5th locked).
#
# [0, 0, 1, 1, 1, 0, 1]
# # You free the prisoner in the 7th cell - and you are done!
#
# Here, we have set free 4 prisoners in total.
#
# Create a function that, given this unique prison arrangement, returns the number of freed prisoners.
# Examples
#
# freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4
#
# freed_prisoners([1, 1, 1]) ➞ 1
#
# freed_prisoners([0, 0, 0]) ➞ 0
#
# freed_prisoners([0, 1, 1, 1]) ➞ 0
#
# Notes
#
# You are the prisoner in the first cell. You must be freed to free anyone else. You must free a prisoner in order
# for the locks to switch. So in the second example where the input is [1, 1, 1] after you release the first
# prisoner, the locks change to [0, 0, 0]. Since all cells are locked, you can release no more prisoners. You always
# start within the leftmost element in the list (the first prison cell). If all the prison cells to your right are
# zeroes, you cannot free any more prisoners.


def freed_prisoner(prison: list):
    cur_cell = 0
    prisoners_free = 0

    if prison[0] == 0:
        return prisoners_free

    while cur_cell != len(prison):
        cur_ind = 0
        if prison[cur_cell] == 0:
            cur_cell += 1
        else:
            if 1 not in prison[1:]:
                prisoners_free += 1
                return prisoners_free
            else:
                prisoners_free += 1
                cur_cell += 1
                while cur_ind != len(prison):
                    if prison[cur_ind] == 1:
                        prison[cur_ind] = 0
                        cur_ind += 1
                    elif prison[cur_ind] == 0:
                        prison[cur_ind] = 1
                        cur_ind += 1

    return prisoners_free


print(freed_prisoner([1, 1, 0, 0, 0, 1, 0]))
print(freed_prisoner([1, 1, 1]))
print(freed_prisoner([0, 0, 0]))
print(freed_prisoner([0, 1, 1, 1]))

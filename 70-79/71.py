# https://edabit.com/challenge/pQavNkBbdmvSMmx5x
# Create a function that returns the majority vote in a list. A
# majority vote is an element that occurs > N/2 times in a list (where N is the length of the list). Examples
#
# majority_vote(["A", "A", "B"]) ➞ "A"
#
# majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"
#
# majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
#
# Notes
#
# The frequency of the majority element must be strictly greater than 1/2.
# If there is no majority element, return None.
# If the list is empty, return None.


def majority_vote(vote_list: list):
    #   establish placeholders
    candidict = {}
    vote_len = len(vote_list) - 1

    #   uniquify list into dict
    while vote_len != -1:
        if vote_list[vote_len] not in candidict:
            candidict[vote_list[vote_len]] = 0
            vote_len -= 1
        else:
            vote_len -= 1

    #   count each vote and add it to the dict
    vote_len = len(vote_list)
    vote_index = vote_len - 1
    while vote_len != 0:
        candidict[vote_list[vote_index]] += 1
        vote_len -= 1
        vote_index = vote_len - 1

    #   check for majority
    for k, v in candidict.items():
        if v > len(vote_list) / 2:
            return k
        else:
            return None


print(majority_vote(["A", "B", "A"]))
print(majority_vote(["A", "A", "A", "B", "C", "A"]))
print(majority_vote(["A", "B", "B", "A", "C", "C"]))

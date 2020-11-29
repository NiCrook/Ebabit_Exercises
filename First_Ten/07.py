#   https://edabit.com/challenge/Zerwo2AENbvRZTe83
#   Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.


def next_edge(edge1: int, edge2: int) -> int:
    max_range = (edge1 + edge2) - 1
    return max_range


print(next_edge(5, 7))

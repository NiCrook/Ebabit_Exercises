#   https://edabit.com/challenge/baBNZFCozmjNhbp9Q
#   Create a function that takes a number (step) as an argument
#   and returns the amount of boxes in that step of the sequence.
#   Step 0: Start with 0
#   Step 1: Add 3
#   Step 2: Subtract 1
#   Repeat Step 1 & 2 ...


def box_seq(steps: int) -> int:
    steps_taken = 0
    boxes = 0
    while steps_taken != steps + 1:
        if steps_taken == 0:
            steps_taken += 1
        elif steps_taken % 2 != 0:
            steps_taken += 1
            boxes += 3
        elif steps_taken % 2 == 0:
            steps_taken += 1
            boxes -= 1
    return boxes


print(box_seq(0))
print(box_seq(1))
print(box_seq(2))
print(box_seq(3))

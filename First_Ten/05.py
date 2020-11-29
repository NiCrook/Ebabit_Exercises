#   https://edabit.com/challenge/nyeNvKWdDFKRAk4Da
#   Write a function that converts hours into seconds.


def hours_to_seconds(hours: float) -> int:
    seconds = (hours * 60) * 60
    return int(seconds)


print(hours_to_seconds(2))

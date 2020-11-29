#   https://edabit.com/challenge/FQyaaJx7orS7tiwz8
#   Write a function that takes an integer minutes and converts it to seconds.


def minute_to_seconds(minutes: float) -> int:
    seconds = (minutes * 60)
    return int(seconds)


print(minute_to_seconds(3.2))

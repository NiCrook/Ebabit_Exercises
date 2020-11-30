#   https://edabit.com/challenge/PjcKZRx8YE5KzRN63
#   Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.


def time_converter(hours: float, minutes: float) -> int:
    total_minutes = (hours * 60) + minutes
    total_seconds = total_minutes * 60
    return int(total_seconds)


print(time_converter(1, 3))

#   https://edabit.com/challenge/XXJbGFEkrMWCp8yFn
#   Write a function that returns the string "something" joined with a space " " and the given argument a.


def give_me_something(message: str) -> str:
    something = "something" + " "
    result = something + message
    return result


print(give_me_something("or nothing at all"))

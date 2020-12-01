#   https://edabit.com/challenge/coRuMC4Ykksti8Z47
#   Create a function that takes a name and returns a greeting in the form of a string.


def hello_name(name: str) -> str:
    greeting = f"Hello {name}!"
    return greeting


print(hello_name("Gerald"))
print(hello_name("Tiffany"))
print(hello_name("Ed"))

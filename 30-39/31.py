#   https://edabit.com/challenge/coRuMC4Ykksti8Z47
#   Create a function that takes a name and returns a greeting in the form of a string.


def hello_name(name: str) -> str:
    try:
        greeting = f"Hello {name}!"
        return greeting
    except TypeError as err:
        print(f"Error: {err}")


print(hello_name("Gerald"))
print(hello_name("Tiffany"))
print(hello_name("Ed"))

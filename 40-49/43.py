#   https://edabit.com/challenge/pFQPcaaASgHuACbaS
#   Given two strings, first_name and last_name, return a single string in the format "last, first".


def concact_name(first_name: str, last_name: str) -> str:
    try:
        result = last_name + ", " + first_name
        return result
    except TypeError as err:
        print(f"Error: {err}")


print(concact_name("First", "Last"))
print(concact_name("John", "Doe"))
print(concact_name("Mary", "Jane"))

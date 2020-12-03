#   https://edabit.com/challenge/owmKG47zYRJw72aiD
#   Given three arguments ⁠— a dictionary obj, a key name and a value
#   return a dictionary with that name and value in it (as key-value pairs).


def add_name(user_dict: dict, name: str, val: int) -> dict:
    try:
        if user_dict:
            user_dict[name] = val
            return user_dict
        else:
            new_dict = {name: val}
            return new_dict
    except TypeError as err:
        print(f"Error: {err}")


print(add_name({}, "Brutus", 300))
print(add_name({"piano": 500}, "Brutus", 400))
print(add_name({"piano": 500, "stereo": 300}, "Caligula", 440))

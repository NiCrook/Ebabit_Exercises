#   https://edabit.com/challenge/q4bBcq5NET4CH5Rcb
#   Jay and Silent Bob have been given a fraction of an ounce but they only understand grams.
#   Convert a fraction passed as a string to grams with up to two decimal places. An ounce weighs 28 grams.


def jay_and_bob(weight: str) -> str:
    try:
        weight_dict = {"ounce": 28, "half": 14, "quarter": 7, "eighth": 3.5, "tenth": 2.8}
        if weight in weight_dict:
            grams = weight_dict[weight]
            return f"{grams} grams"
        else:
            return "Yo, what?"
    except TypeError as err:
        return f"Error: {err}"


print(jay_and_bob("ounce"))
print(jay_and_bob("half"))
print(jay_and_bob("quarter"))
print(jay_and_bob("eighth"))
print(jay_and_bob("tenth"))
print(jay_and_bob("pound"))

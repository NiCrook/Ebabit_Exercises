#   https://edabit.com/challenge/gt9LLufDCMHKMioh2
#   Write a function that stutters a word as if someone is struggling to read it.
#   The first two letters are repeated twice with an ellipsis ... and space after each,
#   and then the word is pronounced with a question mark ?.


def stutter(word_to_stutter: str) -> str:
    try:
        stutter = word_to_stutter[0:2] + "... "
        result = (stutter * 2) + word_to_stutter + "?"
        return result
    except TypeError as err:
        print(f"Error: {err}")


print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))

#   https://edabit.com/challenge/JzBLDzrcGCzDjkk5n
#   Make a function that encrypts a given input with these steps:
#
#   Input: "apple"
#   Step 1: Reverse the input: "elppa"
#   Step 2: Replace all vowels using the following chart:
#   a => 0
#   e => 1
#   i => 2
#   o => 2
#   u => 3
#   "1lpp0"
#   Step 3: Add "aca" to the end of the word: "1lpp0aca"
#   Output: "1lpp0aca"
#   Examples
#   encrypt("banana") ➞ "0n0n0baca"
#   encrypt("karaca") ➞ "0c0r0kaca"
#   encrypt("burak") ➞ "k0r3baca"
#   encrypt("alpaca") ➞ "0c0pl0aca"
#   All inputs are strings, no uppercases and all output must be strings.
VOWEL_DICT = {
    "a": 0,
    "e": 1,
    "i": 2,
    "o": 2,
    "u": 3
}

END_STR = "aca"


def encrypt(unenc_str: str):
    unenc_str = unenc_str.lower()
    str_list = []

    while len(unenc_str) != 0:
        str_list.append(unenc_str[0])
        unenc_str = unenc_str[1:]
    str_list_len = len(str_list) - 1
    while str_list_len != -1:
        if str_list[str_list_len] in VOWEL_DICT.keys():
            str_list[str_list_len] = VOWEL_DICT[str_list[str_list_len]]
            str_list_len -= 1
        else:
            str_list_len -= 1
    list_to_str = "".join(str(x) for x in str_list)
    ending_string = list_to_str + END_STR
    return ending_string


print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))

# https://edabit.com/challenge/7Y2C8g3fXXyK2R9Bn
#
# A Keyword Cipher is a monoalphabetic cipher which uses a keyword to provide encryption on given string of message.
#
# Create a function that takes two arguments; a string of message and a string of key and returns an encoded message.
#
# There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:
#
# message = "ABCHIJ"
# key = "KEYWORD"
#
# keyword_cipher(key, message) ➞ "KEYABC"
#
# Write all alphabets from A to Z:
#
# All alphabets which are part of keyword are removed and the alphabets are re-arranged such that keyword appears
# first, followed by the rest of the alphabets in usual order.
#
#
# Return all alphabets of key against given message:
#
# eMessage = "KEYABC"
# // A = K, B = E, C = Y, H = A, I = B, J = C
#
# Examples
#
# keyword_cipher("keyword", "abchij") ➞ "keyabc"
#
# keyword_cipher("purplepineapple", "abc") ➞ "pur"
#
# keyword_cipher("mubashir", "edabit") ➞ "samucq"
#
# Notes
#
#     Don't forget to remove duplicates after concatenating string with keyword.
#     Take care of characters other than alphabets.

# get keyword and compare to alpha_list
# while len(key) != 0:
# if keyword[0] in alpha_list:
# new_alpha_list = alpha_list[key[0]].pop + alpha_list
# keyword = keyword[1:]
import string


def keyword_cipher(key: str, message: str):
    index = 0
    alpha_index = 0
    seen_characters = ""
    cipher_string = ""
    alpha_list = list(string.ascii_lowercase)
    alpha_cipher_list = alpha_list

    while len(key) != 0:
        if key[0] in alpha_list:
            if key[0] == alpha_cipher_list[index]:
                if key[0] not in seen_characters:
                    alpha_cipher_list.insert(alpha_index, alpha_cipher_list.pop(index))
                    index = 0
                    alpha_index += 1
                    seen_characters += key[0]
                    key = key[1:]
                else:
                    index = 0
                    alpha_index += 1
                    key = key[1:]
            else:
                index += 1
        else:
            index = 0
            alpha_index += 1
            key = key[1:]

    index = 0
    alpha_index = 0
    alpha_list = list(string.ascii_lowercase)

    while len(cipher_string) != len(message):
        if message[index] == alpha_list[alpha_index]:
            cipher_string += alpha_cipher_list[alpha_index]
            index += 1
            alpha_index = 0
        else:
            alpha_index += 1

    return cipher_string


print(keyword_cipher("keyword", "abchij"))
print(keyword_cipher("purplepineapple", "abc"))
print(keyword_cipher("mubashir", "edabit"))

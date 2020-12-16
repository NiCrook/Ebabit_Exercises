# https://edabit.com/challenge/MGALfBAXhXqqdFyqo
#
# The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in
# the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
#
# Create a function that takes a string and applies the Atbash cipher to it.
# Examples
#
# atbash("apple") ➞ "zkkov"
#
# atbash("Hello world!") ➞ "Svool dliow!"
#
# atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
#
# Notes
#
#     Capitalisation should be retained.
#     Non-alphabetic characters should not be altered.
ALPHA_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']


def atbash(word: str):
    word_list = list(word)
    cipher = ""
    cur_ind = 0
    while len(word_list) != 0:
        if word_list[-1].isupper():
            if word_list[-1] == ALPHA_LIST[cur_ind]:
                cur_ind += 1
                cur_ind *= -1
                cipher_char = ALPHA_LIST[cur_ind]
                cipher = cipher_char + cipher
                del word_list[-1]
                cur_ind = 0
            else:
                cur_ind += 1
        elif word_list[-1].islower():
            cipher_len = len(cipher)
            while cipher_len == len(cipher):
                word_list[-1] = word_list[-1].upper()
                if word_list[-1] == ALPHA_LIST[cur_ind]:
                    cur_ind += 1
                    cur_ind *= -1
                    cipher_char = ALPHA_LIST[cur_ind].lower()
                    cipher = cipher_char + cipher
                    cur_ind = 0
                    del word_list[-1]
                else:
                    cur_ind += 1
        else:
            cipher = word_list[-1] + cipher
            del word_list[-1]

    return cipher


print(atbash("apple"))
print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))

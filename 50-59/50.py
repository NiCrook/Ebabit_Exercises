#   https://edabit.com/challenge/2zKetgAJp4WRFXiDT
#   Create a function that takes a number num and returns its length.
#   DO NOT USE LEN() FOR THIS CHALLENGE


def number_length(num1: int) -> int:
    try:
        str_num = str(num1)
        current_len = 0
        while str_num != "":
            current_len += 1
            str_num = str_num[1:]
        return current_len
    except TypeError as err:
        print(f"Error: {err}")


print(number_length(10))
print(number_length(5000))
print(number_length(0))

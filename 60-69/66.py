#   https://edabit.com/challenge/7PtLRCT5aL9uiqxPs
#   Your job is to create a function that takes 3 numbers: a, b, c
#   and returns True if the last digit of a * b = the last digit of c.


def last_dig(num1: int, num2: int, num3: int) -> bool:
    last_one = int(repr(num1)[-1])
    last_two = int(repr(num2)[-1])
    last_three = int(repr(num3)[-1])
    product = last_one * last_two
    last_product = int(repr(product)[-1])
    if last_product == last_three:
        return True
    else:
        return False


print(last_dig(25, 21, 125))
print(last_dig(55, 226, 5190))
print(last_dig(12, 215, 2142))

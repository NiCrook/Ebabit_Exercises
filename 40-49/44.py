#   https://edabit.com/challenge/aj7JPnAuW8dy4ggdp
#   Write a function that returns the string "even" if the given integer is even, and the string "odd" if it's odd.


def even_or_odd(num1: int) -> str:
    try:
        if not num1 % 2:
            return "Even"
        return "Odd"
    except TypeError as err:
        print(f"Error: {err}")


print(even_or_odd(6))
print(even_or_odd(5))

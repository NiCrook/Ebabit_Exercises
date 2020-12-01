#   https://edabit.com/challenge/pKyeEDkNqZraqS3rW
#   Write a function that returns True if k^k == n for input (n, k) and return False otherwise.


def exponator(k: int, n: int) -> bool:
    try:
        expo = n ** n
        if expo == k:
            return True
        else:
            return False
    except TypeError as err:
        print(f"Error: {err}")


print(exponator(4, 2))
print(exponator(387420489, 9))
print(exponator(3124, 5))
print(exponator(17, 3))

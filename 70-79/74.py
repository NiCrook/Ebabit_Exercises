# https://edabit.com/challenge/kKFuf9hfo2qnu7pBe
# 
# Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in 
# your function. The target number will be from 2 through 97. If the target is prime then return "yes" else return 
# "no". Examples 
# 
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 
# 
# is_prime(primes, 3) ➞ "yes"
# 
# is_prime(primes, 4) ➞ "no"
# 
# is_prime(primes, 67) ➞ "yes"
# 
# is_prime(primes, 36) ➞ "no"
# 
# Notes
# 
# You could use built-in functions to solve this, but the point of this challenge is to see if you understand the 
# binary search algorithm. The solution is in the Resources tab. 


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def is_prime(prime_list: list, num1: int):
    half = len(PRIMES) / 2
    half = int(half)

    if num1 < half:
        while half != 0:
            if num1 == PRIMES[half]:
                return "yes"
            else:
                half -= 1
        if half == 0:
            return "no"

    if num1 > half:
        while half != len(PRIMES):
            if num1 == PRIMES[half]:
                return "yes"
            else:
                half += 1
        if half == len(PRIMES):
            return "no"


print(is_prime(PRIMES, 3))
print(is_prime(PRIMES, 4))
print(is_prime(PRIMES, 67))
print(is_prime(PRIMES, 36))

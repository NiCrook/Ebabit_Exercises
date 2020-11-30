#   https://edabit.com/challenge/QzXtDnSZL6y4ZcEvT
#   In this challenge, a farmer is asking you to tell him
#   how many legs can be counted among all his animals.
#   chicken = 2 legs, cow = 4 legs, pigs = 4 legs
#   The farmer has counted his animals
#   he gives you a subtotal for each species.
#   You have to implement a function that returns the total number of legs of all the animals.


def leg_counter(chickens: int, cows: int, pigs: int) -> int:
    chicken_legs = chickens * 2
    cow_legs = cows * 4
    pig_legs = pigs * 4
    total_legs = chicken_legs + cow_legs + pig_legs
    return total_legs


print(leg_counter(2, 3, 5))

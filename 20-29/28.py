#   https://edabit.com/challenge/SNM5EZ3FePECt2HQn
#   Create a function that takes three arguments prob, prize, pay
#   returns True if prob * prize > pay; otherwise return False.


def profitable_gambe(prob: float, prize: float, pay: float) -> bool:
    try:
        result = prob * prize
        if result > pay:
            return True
        else:
            return False
    except ValueError as err:
        print(f"Error: {err}")


print(profitable_gambe(0.2, 50, 9))
print(profitable_gambe(0.9, 1, 2))
print(profitable_gambe(0.9, 3, 2))

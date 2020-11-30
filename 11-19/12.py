#   https://edabit.com/challenge/v5gc8FQkDEepkqpfp
#   Create a function that takes voltage and current and returns the calculated power.
#   Power = voltage x current


def circuit_power(voltage: int, current: int) ->  int:
    power = voltage * current
    return power


print(circuit_power(230, 10))

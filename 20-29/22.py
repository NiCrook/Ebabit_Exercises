#   https://edabit.com/challenge/yfooETHj3sHoHTJsv
#   Create a function that returns True when num1 is equal to num2; otherwise return False.


def same_thing(int1: int, int2: int) -> bool:
    try:
        if int1 == int2:
            return True
        elif int1 != int2:
            return False
    except ValueError as err:
        print(f"Error: {err}")


print(same_thing(4, 4))
print(same_thing(5, 9))

#   https://edabit.com/challenge/2RtztnzMDdyAj2MD3
#   Create a function that takes two number strings and returns their sum as a string.


def adder(num1: str, num2: str) -> str:
    try:
        def num_str_adder() -> str:
            try:
                result = int(num1) + int(num2)
                return str(result)
            except ValueError:
                return "Invalid Operation"

        return num_str_adder()
    except TypeError:
        return "Invalid Operation"


print(adder("111", "111"))
print(adder("10", "80"))
print(adder("", "20"))

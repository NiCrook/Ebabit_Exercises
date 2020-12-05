#   https://edabit.com/challenge/ta8GBizBNbRGo5iC6
#   Create methods for the Calculator class that can do the following:
#
#     Add two numbers.
#     Subtract two numbers.
#     Multiply two numbers.
#     Divide two numbers.


class Calculator:
    def add(self, n1: int, n2: int) -> int:
        add_result = n1 + n2
        return add_result

    def subtract(self, n1: int, n2: int) -> int:
        sub_result = n1 - n2
        return sub_result

    def multiply(self, n1: int, n2: int) -> int:
        mul_result = n1 * n2
        return mul_result

    def divide(self, n1: int, n2: int) -> int or float:
        div_result = n1 / n2
        if div_result % 2 == 0:
            return int(div_result)
        else:
            return div_result


calculamator = Calculator()
print(calculamator.add(10, 5))
print(calculamator.subtract(10, 5))
print(calculamator.multiply(10, 5))
print(calculamator.divide(10, 5))

#   Create a function that takes two numbers as arguments (num, length)
#   and returns a list of multiples of num until the list length reaches length.
#   Notice that num is also included in the returned list.
import typing


def list_of_multiples(num: int, length: int) -> typing.List[int]:
    try:
        result = 0
        result_list = []
        while result != length:
            result += 1
            multiple = num * result
            result_list.append(multiple)
        return result_list
    except TypeError as err:
        print(f"Error: {err}")


print(list_of_multiples(7, 5))
print(list_of_multiples(12, 10))
print(list_of_multiples(17, 6))

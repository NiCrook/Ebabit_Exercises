#   https://edabit.com/challenge/inPpSzkuRCocLM3x2
#   Create a function that takes an array arr and a number n
#   and returns an array of two integers from arr whose product is that of the number n of the following form:
#   [value_at_lower_index, value_at_higher_index]


def two_product(list1: list, num1: int) -> list:
    try:
        a = 0
        b = 1
        empty_list = []
        while a != len(list1) - 1:
            while b != len(list1):
                if list1[a] * list1[b] == num1:
                    empty_list.append(list1[a])
                    empty_list.append(list1[b])
                    return empty_list
                else:
                    b += 1
            else:
                a += 1
                b = a + 1
        return empty_list
    except TypeError as err:
        print(f"Error: {err}")


print(two_product([1, 2, -1, 4, 5], 20))
print(two_product([1, 2, 3, 4, 5], 10))
print(two_product([100, 12, 4, 1, 2], 15))

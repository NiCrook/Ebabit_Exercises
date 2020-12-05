#   https://edabit.com/challenge/WXqH9qvvGkmx4dMvp
#   Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
#     If the number is a multiple of 3 the output should be "Fizz".
#     If the number given is a multiple of 5, the output should be "Buzz".
#     If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
#     If the number is not a multiple of either 3 or 5,
#     the number should be output on its own as shown in the examples below.
#     The output should always be a string even if it is not a multiple of 3 or 5.


def fizz_buzz(num_: int) -> str:
    try:
        fizz = "Fizz"
        buzz = "Buzz"
        fibu = "FizzBuzz"
        no_fizz = f"{num_}"
        if num_ % 5 == 0 and num_ % 3 == 0:
            return fibu
        elif num_ % 5 == 0:
            return buzz
        elif num_ % 3 == 0:
            return fizz
        else:
            return no_fizz
    except TypeError as err:
        print(f"Error: {err}")


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))

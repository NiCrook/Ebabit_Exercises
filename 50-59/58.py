#   https://edabit.com/challenge/xR248CxGSsSrNK5Za
#   Write a function that accepts the width and height (m, n)
#   and an optional proc s and generates a list with m elements.
#   Each element is a string consisting of either:
#
#   The default character (hash #) repeating n times (if no proc is given).
#   The character passed in through the proc repeating n times.


def make_rug(width: int, height: int, proc="") -> list:
    rug = []

    def row_maker():
        if proc:
            row = proc * height
            return row
        else:
            row = "#" * height
            return row

    if not rug:
        while len(rug) != width:
            new_row = row_maker()
            rug.append(new_row)

    return rug


print(make_rug(3, 5))
print(make_rug(3, 5, "$"))
print(make_rug(2, 2, "A"))

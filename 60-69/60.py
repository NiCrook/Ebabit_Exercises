#   https://edabit.com/challenge/X6xZ2EaqqQbGF7Bwv
#   Given an int, figure out how many ones, threes and nines you could fit into the number.
#   You must create a class.
#   You will make variables (self.ones, self.threes, self.nines) to do this.
#   Do not use the math module.


class OnesNinesThrees:
    def __init__(self, num1: int):
        self.num1 = num1
        self.ones = 0
        self.threes = 0
        self.nines = 0

    def find_ones(self) -> int:
            self.ones = self.num1 / 1
            self.ones = int(self.ones)
            return self.ones

    def find_threes(self) -> int:
            self.threes = self.num1 / 3
            self.threes = int(self.threes)
            return self.threes

    def find_nines(self) -> int:
            self.nines = self.num1 / 9
            self.nines = int(self.nines)
            return self.nines


finder = OnesNinesThrees(5)
print(finder.find_ones())
print(finder.find_threes())
print(finder.find_nines())

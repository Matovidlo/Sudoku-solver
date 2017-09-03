#! /usr/bin/env python3

"""
    Author: tammar96
    Brief:  Simple sudoku solver and generator
"""

class Field():

    def __init__(self):
        self.value = 0
        self.follow = list(range(1, 9))

    def __setValue(self, val):
        if (val > 0 and val < 10):
            self.value = val
        return false

    def getValue(self):
        return self.value

    value = None
    follow = list()
    evalueatable = True

class Sudoku():

    def __init__(self):
        "constructor"

    def __str__(self):
        "create string from this object"
        ret = ""

        for x in range(9):
            for y in range(9):
                ret = ret + str(self.gameArray[x][y].getValue()) + " "
                if y is 3:
                    print("\b|")
            ret = ret + "\n"

        return ret

    def create(self, difficulity):
        "docstring"
        return None

    def solve(self):
        "docstring"
        return None

    def printf(self):
        "docstring"
        # print(self.gameArray)
        return None

    gameArray = [[Field()]*9 for i in range(9)]


def main():
    sudoku = Sudoku()
    print(sudoku)
    return None

if __name__ == "__main__":
    main()

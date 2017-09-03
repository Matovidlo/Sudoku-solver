#! /usr/bin/env python3

"""
    Author: tammar96
    Brief:  Simple sudoku solver and generator
"""

class Field():

    def __init__(self):
        self.value = 0

    def setValue(self, val):
        self.value = val

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

        for x in 9:
            for y in 9:
                ret.append(self.gameArray[x][y].value)
            ret.append("\n")

        return ret

    def create(self):
        "docstring"
        return None

    def solve(self):
        "docstring"
        return None

    def print(self):
        "docstring"
        print(self.gameArray)
        return None

    gameArray = [[Field()]*9 for i in range(9)]


def main():
    sudoku = Sudoku()
    sudoku.print()
    return None

if __name__ == "__main__":
    main()

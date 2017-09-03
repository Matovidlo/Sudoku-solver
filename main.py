#! /usr/bin/env python3

"""
    Author: tammar96
    Brief:  Simple sudoku solver and generator
"""


class Sudoku():

    def __init__(self):
        "constructor"

    def __str__(self):
        "create string from this object"

    def create(self):
        "docstring"
        return None

    def solve(self):
        "docstring"
        return None

    def print(self):
        "docstring"
        return None

    gameArray = [[Field(0)]*9 for i in range(9)]

class Field():

    def __init__(self, v):
        self.value = v

    def __init__(self):
        self.value = 0

    value = None
    follow = list()
    evalueatable = True

def main():
    return None

if __name__ == "__main__":
    main()

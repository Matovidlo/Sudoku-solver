#! /usr/bin/env python3

"""
    Author: tammar96
    Brief:  Simple sudoku solver and generator
"""

class Field():

    def __init__(self):
        self.value = 0
        self.follow = list(n + 1 for n in range(9))

    def __setValue(self, val):
        if val > 0 and val < 10:
            self.value = val
            return True
        return False

    def removeItem(self, item):
        self.follow.remove(item)

    def setFollow(self, follow):
        if len(follow) is 1:
            self.value = follow[0]
        self.evalueatable = False
        self.follow = follow

    def checkFollow(self):
        if len(self.follow) is 1:
            self.__setValue(self.follow[0])

    def getValue(self):
        return self.value

    value = None
    follow = list()
    evalueatable = True

class Sudoku():

    gameArray = None

    def __init__(self):
        "constructor"
        self.gameArray = [[Field()]*9 for i in range(9)]

    def __str__(self):
        "create string from this object"
        ret = "\n"

        for x in range(9):
            for y in range(9):
                ret = ret + str(self.gameArray[x][y].value) + " "
                if y % 3 is 2 and y is not 8:
                    ret = ret + "| "
            ret = ret + "\n"
            if x % 3 is 2 and x is not 8:
                ret = ret + "---------------------\n"

        return ret

    def create(self, difficulity):
        "docstring"
        return None

    def getFollow(self, x, y):

        follow = list()

        for i in range(9):
            if self.gameArray[x][i].value is not 0 and self.gameArray[x][i].value not in follow:
                follow.append(self.gameArray[x][i].value)

        for i in range(9):
            if self.gameArray[i][y].value is not 0 and self.gameArray[x][i].value not in follow:
                follow.append(self.gameArray[i][y].value)

        minx = 0
        miny = 0

        if x >= 3 and x < 6:
            minx += 3
        elif x >= 6:
            minx = +6

        if y >= 3 and y < 6:
            minx += 3
        elif y >= 6:
            minx = +6

        for xx in range(3):
            tempx = xx + minx
            for yy in range(3):
                tempy = yy + miny
                if self.gameArray[tempx][tempy].value is not 0 and self.gameArray[x][i].value not in follow:
                    follow.append(self.gameArray[tempx][tempy].value)

        return follow

    def solve(self):
        "docstring"

        for x in range(9):
            for y in range(9):
                if self.gameArray[x][y].evalueatable is True:
                    follow = self.getFollow(x, y)
                    self.gameArray[x][y].setFollow(follow)

        return None

    def print2pdf(self):
        "docstring"
        # print(self.gameArray)
        return None

def main():
    sudoku = Sudoku()
    print(sudoku)
    return None

if __name__ == "__main__":
    main()

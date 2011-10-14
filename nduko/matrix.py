#!/usr/bin/env python
import random

class Matrix(object):
    def __init__(self):
        self.dataStructure = {}

    def __str__(self):
        return str(self.dataStructure)
        
    def setItem(self, r, c, value):
        try:
            self.dataStructure[c][r] = value 
        except KeyError:
            self.dataStructure[c] = {r:value}

    def getItem(self, r, c):
        return self.dataStructure[c][r]

    def removeColumn(self, c):
        return None

    def addRandomColumn(self):
        column = [random.randint(0, 1) for i in range(5)]
        self.dataStructure[len(self.dataStructure) + 1] = [column]

if __name__ == '__main__':
    m = Matrix()
    #sets the item in row 0, column 0 to 1
    #m.setItem(0, 0, 1)
    #print m.getItem(0, 0)
    #print m

    #add 5 random columns
    for i in range(5):
        m.addRandomColumn()
    print m 

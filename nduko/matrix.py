#!/usr/bin/env python
import random

class Matrix(object):
    def __init__(self):
        self._dataStructure = {}

    def __str__(self):
        return str(self._dataStructure)

    def __iter__(self):
        return iter(self._dataStructure)

    def __len__(self):
        return len(self._dataStructure)
        
    def setItem(self, r, c, value):
        try:
            self._dataStructure[c][r] = value 
        except KeyError:
            self._dataStructure[c] = {r:value}

    def setColumn(self, c, column):
        self._dataStructure[c] = column

    def column(self, c):
        return self._dataStructure[c]

    def getItem(self, r, c):
        return self._dataStructure[c][r]

    def removeColumn(self, c):
        newMatrix = Matrix() 
        for k in self:
            if k != c:
                newMatrix.setColumn(k, self.column(c))
        return newMatrix

    def addRandomColumn(self):
        column = [random.randint(0, 1) for i in range(5)]
        self.setColumn(len(self) + 1, column)

if __name__ == '__main__':
    m = Matrix()
    #sets the item in row 0, column 0 to 1
    #m.setItem(0, 0, 1)
    #print m.getItem(0, 0)
    #print m

    #add 5 random columns
    for i in range(5):
        m.addRandomColumn()
    print 'initial state:', m 
    print 'removed column 2', m.removeColumn(2)

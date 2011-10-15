#!/usr/bin/env python
import random

class Matrix(object):
    '''A class representing a simple matrix'''
    def __init__(self):
        self._dataStructure = {}

    def __str__(self):
        '''Return the string representation of the matrix'''
        return str(self._dataStructure)

    def __iter__(self):
        '''Return an iter object for the matrix'''
        return iter(self._dataStructure)

    def __len__(self):
        '''Return the length (in columns) of the matrix'''
        return len(self._dataStructure)
        
    def setItem(self, r, c, value):
        '''Set the value of the item in the column c and the row r to the value
        of value'''
        try:
            self._dataStructure[c][r] = value 
        except KeyError:
            self._dataStructure[c] = {r:value}

    def setColumn(self, c, column):
        '''Set an entire colunm c to have the values of column. Column should
        be a List'''
        self._dataStructure[c] = column

    def column(self, c):
        '''Return the column c'''
        return self._dataStructure[c]

    def getItem(self, r, c):
        '''Return the value of the item at column c and row r'''
        return self._dataStructure[c][r]

    def removeColumn(self, c):
        '''Return a copy of the matrix with the column c removed'''
        newMatrix = Matrix() 
        for k in self:
            if k != c:
                newMatrix.setColumn(k, self.column(c))
        return newMatrix

    def addRandomColumn(self):
        '''Add a column full of random 1s and 0s (used for testing)'''
        column = [random.randint(0, 1) for i in range(5)]
        self.setColumn(len(self) + 1, column)

if __name__ == '__main__':
    '''Do some self testing'''
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

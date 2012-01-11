#!/usr/bin/env python
import random
import json
import pprint as pp

class Matrix(object):
    '''A class representing a simple matrix'''
    rowsTaken = {}
    def __init__(self):
        self._dataStructure = {}

    def __str__(self):
        '''Return the string representation of the matrix'''
        return pp.pformat(self._dataStructure)

    def __iter__(self):
        '''Return an iter object for the matrix'''
        return iter(self._dataStructure)

    def __len__(self):
        '''Return the length (in columns) of the matrix'''
        return len(self._dataStructure)

    def __getitem__(self, c):
        '''Return the column c'''
        return self.column(c)
        
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

    def column(self, r):
        '''Return the row r'''
        return [self[c][r] for c in self]
    
    def row(self, c):
        '''Return the column c'''
        return self._dataStructure[c]

    def columns(self):
        '''Return the names of each column'''
        return self._dataStructure.keys()

    def getItem(self, r, c):
        '''Return the value of the item at column c and row r'''
        return self._dataStructure[c][r]

    def removeColumn(self, c):
        '''Return a copy of the matrix with the column c removed'''
        newMatrix = Matrix() 
        for k in self:
            if k != c:
                newMatrix.setColumn(k, self.column(k))
        return newMatrix

    def removeRow(self, r):
        '''Return a copy of the matrix with the row r removed'''
        newMatrix = Matrix()
        for c in self:
            newMatrix.setColumn(c, self.column(c))
            del newMatrix[c][r]
        return newMatrix

    def addRandomColumn(self):
        '''Add a column full of random 1s and 0s (used for testing)'''
        column = [0 for i in range(5)]
        #do a bit of a hack
        c = random.randint(0, len(column))
        while c in self.rowsTaken:
            self.rowsTaken[random.randint(0, len(column))] = 1
        column[c] = 1
        #column[] = 1
        self.setColumn(len(self), column)

    def load(self, filename):
        '''Load the data stored in filename as json'''
        with open(filename) as f:
            self._dataStructure = json.load(f)

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
    print 'removed row 2', m.removeRow(2)
    print 'row 0', m.row(0)
    print 'column 0', m.column(0)

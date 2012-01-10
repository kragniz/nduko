#!/usr/bin/env python

from matrix import Matrix
import random
import pprint as pp

class ExactCover(object):
    def __init__(self):
        self._matrix = Matrix()
        self.solution = []
        #self._rows = []
        #for i in range(5):
        #    self._matrix.addRandomColumn()

    def __str__(self):
        return pp.pprint(self._matrix)

    def load(self, filename):
        '''Wrapper for Matrix.load'''
        self._matrix.load(filename)

    def solve(self, A, depth=-1):
        '''Solve the exact cover problem on the matrix A'''
        #If the matrix A is empty, the problem is solved; terminate
        #successfully.
        print '###################'
        print A
        if len(A) == 0:
            #we have completed the problem, return the result
            return True

        #Otherwise choose a column c (deterministically) as the column with
        #the smallest number of 1s. Return False if any column has no 1s.
        c = A.column(A.columns()[0])
        smallest = 0
        for i in A:
            columnSum = sum(A[i])
            if columnSum == 0:
                print A[i], 'has no 1s'
                return False
            else:
                if columnSum > smallest:
                    smallest = i
                    c = A.column(A.columns()[int(i)])

        print 'c:', c
        rows = []
        #Choose a row r such that A(r, c) = 1
        for i, r in enumerate(c):
            if r == 1:
                rows += [i]
        print 'r:', rows
             
        #Include row r in the partial solution, if a solution
        #exists.
        if len(rows):
            r = random.randint(0, len(rows))
            #print 'r =', r
            self.solution += [rows[r-1]]

        #For each column j such that A(r, j) = 1,
        for j in A.columns():
            columnj = A[j]
            if r < len(columnj):
                print 'columnj:', columnj, columnj[r]
                if columnj[r] == 1:
                    print 'r == 1'
                    #print columnj
                    #for each row i such that Ai, j = 1
                    for i in range(len(columnj)):
                        #print 'i =', i, 'A[%s]' % i, '=', columnj
                    
                        if i < len(columnj):
                            if columnj[i] == 1:
                                #delete row i from matrix A
                                A = A.removeRow(i)
                    #delete column j from matrix A
                    A = A.removeColumn(j)


        print 'at recursion depth:', depth, 'A:', A
        print 'current solution:', self.solution

        #Repeat this algorithm recursively on the reduced matrix A.
        return self.solve(A, depth)

    def matrix(self):
        return self._matrix

if __name__ == '__main__':
    X = ExactCover()
    X.load('../data/placement.json')
    print X.matrix()
    try:
        print X.solve(X.matrix())
    except RuntimeError:
        print 'cannot solve'
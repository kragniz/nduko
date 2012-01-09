#!/usr/bin/env python

from matrix import Matrix
import random
import pprint as pp

class ExactCover(object):
    def __init__(self):
        self._matrix = Matrix()
        self.solution = []
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
        if len(A) == 0:
            #we have completed the problem, return the result
            return self.solution
        else:
            depth += 1 
            if depth > 50:
                return A

            #Otherwise choose a column c (deterministically).
            c = A.column(A.columns()[0])
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
                self.solution += [self.matrix().row(r)]

            #For each column j such that A(r, j) = 1,
            for j in A.columns():
                columnj = A[j]
                if r < len(columnj):
                    if columnj[r] == 1:
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
    X.load('../data/exactCover.json')
    print X.matrix()
    try:
        print X.solve(X.matrix())
    except RuntimeError:
        print 'cannot solve'
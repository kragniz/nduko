#!/usr/bin/env python

from matrix import Matrix
import random

class ExactCover(object):
    def __init__(self):
        self._matrix = Matrix()
        for i in range(5):
            self._matrix.addRandomColumn()


    def loadFromFile(self, filename):
        coverProblem 

    def solve(self, A, depth=-1):
        '''Solve the exact cover problem on the matrix A'''
        #If the matrix A is empty, the problem is solved; terminate
        #successfully.
        if len(A) == 0:
            #we have completed the problem, return the result
            return A
        else:
            solution = []
            depth += 1 
            if depth > 1000:
                return A
            print 'at recursion depth:', depth, 'A:', A

            #Otherwise choose a column c (deterministically).
            c = A.column(A.columns()[0])
            rows = []
            #Choose a row r such that A(r, c) = 1
            for r in range(len(c)):
                if c[r] == 1:
                    #print self.matrix().row(r)
                    rows += [r]
                 
            #Include row r in the partial solution, if a solution
            #exists.
            if len(rows):
                r = random.randint(0, len(rows))
                #print 'r =', r
                solution = self.matrix().row(r)

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

            #Repeat this algorithm recursively on the reduced matrix A.
            return self.solve(A, depth)

                        
    def matrix(self):
        return self._matrix

if __name__ == '__main__':
    X = ExactCover()
    #print X.matrix()
    try:
        print X.solve(X.matrix())
    except:
        print 'cannot solve'

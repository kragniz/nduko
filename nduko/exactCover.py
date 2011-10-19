#!/usr/bin/env python

from matrix import Matrix
from random import choice

class ExactCover(object):
    def __init__(self):
        self._matrix = Matrix()
        for i in range(5):
            self._matrix.addRandomColumn()

    def solve(self, A):
        '''Solve the exact cover problem on the matrix A'''
        #If the matrix A is empty, the problem is solved; terminate
        #successfully.
        if len(A) == 0:
            #we have completed the problem, return the result
            return A
        else:
<<<<<<< Updated upstream
            solution = []
            
=======
            #Otherwise choose a column c (deterministically).
>>>>>>> Stashed changes
            c = A.column(A.columns()[0])
            rows = []
            #Choose a row r such that A(r, c) = 1
            for r in range(len(c)):
                if c[r] == 1:
                    print self.matrix().row(r)
                    #Include row r in the partial solution.
                    rows += [r]
<<<<<<< Updated upstream
                    
            if len(rows):
                solution = self.matrix().row(choice(rows))
=======
            print choice(rows)
            #For each column j such that A(r, j) = 1,
            for j in 
>>>>>>> Stashed changes
                        
    def matrix(self):
        return self._matrix

if __name__ == '__main__':
    X = ExactCover()
    print X.matrix()
    print X.solve(X.matrix())

#!/usr/bin/env python

import matrix
from random import choice

class ExactCover(object):
    def __init__(self):
        self._matrix = matrix.Matrix()
        for i in range(5):
            self._matrix.addRandomColumn()

    def solve(self, A):
        '''Solve the exact cover problem on the matrix A'''
        if len(A) == 0:
            #we have completed the problem, return the result
            return A
        else:
            c = A.column(A.columns()[0])
            rows = []
            for r in range(len(c)):
                print r
                if c[r] == 1:
                    print self.matrix().row(r)
                    rows += [r]
            print choice(rows)
                        
    def matrix(self):
        return self._matrix

if __name__ == '__main__':
    X = ExactCover()
    print X.matrix()
    print X.solve(X.matrix())

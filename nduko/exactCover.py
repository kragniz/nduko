#!/usr/bin/env python

import matrix

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
            C = A.column(A.columns()[0])
            print C
                        
    def matrix(self):
        return self._matrix

if __name__ == '__main__':
    X = ExactCover()
    print X.matrix()
    print X.solve(X.matrix())

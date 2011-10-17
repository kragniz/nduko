#!/usr/bin/env python

import matrix

class ExactCover(object):
    def __init__(self):
        self._matrix = matrix.Matrix()

    def solve(self, A):
        '''Solve the exact cover problem on the matrix A'''
        if len(A) == 0:
            #we have completed the problem, return the result
            return A
        else:
            
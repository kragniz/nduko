#!/usr/bin/env python

from exactCover import ExactCover

class NdukoSolver(ExactCover):
    def __init__(self, n):
        super(NdukoSolver, self).__init__()

    def valueAt(self, r, c):
    	'''Return the value from the solution at the position row, column'''
    	pass

if __name__ == '__main__':
    solver = NdukoSolver()
    solver.load('../data/nduko')
    try:
        print solver.solve()
    except RuntimeError:
        print 'cannot solve'
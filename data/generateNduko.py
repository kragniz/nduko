#!/usr/bin/env python

import sys, os

class GenerateNduko(object):
    def __init__(self, n):
    	with open('../data/generatedNduko', 'w') as f:
			for i in range(n):
				for j in range(n):
					f.write('%s %s\n' % (i, j))

if __name__ == '__main__':
	g = GenerateNduko(25)
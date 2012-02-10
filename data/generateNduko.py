#!/usr/bin/env python

import sys, os

class GenerateNduko(object):
    def __init__(self, n):
        self.output = open('../data/generatedNduko', 'w')

        cellValue = 0
        rowOffset = 0

        for i in range(n**4):
            for j in range(n**2):
                self.output.write('{0} {1}\n'.format(cellValue, rowOffset))
            cellValue += 1
            if not (i % n**4):
                rowOffset += n**2

if __name__ == '__main__':
    g = GenerateNduko(2)
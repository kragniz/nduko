#!/usr/bin/env python

import sys, os

class GenerateNduko(object):
    def __init__(self, n):
        self.output = open('../data/generatedNduko', 'w')

        for i in range(n**2):
            for j in range(n):

if __name__ == '__main__':
    g = GenerateNduko(25)
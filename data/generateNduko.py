#!/usr/bin/env python

class GenerateNduko(object):
    def __init__(self, n):
        self.n = n
        self.output = open('../data/generatedNduko', 'w')

        cellValue = 0
        rowOffset = 0

        for i in range(n**4):
            for j in range(n**2):
                self.output.write('{0} {1} {2}\n'.format(cellValue,
                                                     n**4 + (rowOffset * n**2 + (j % n**2)),
                                                     2*(n**4) + (n*i % n**3)*n + j) )
            cellValue += 1
            if (i+1) % (n**2) == 0:
                rowOffset += 1
        self.output.close()

    def writeViewable(self):
        with open('../data/viewableNduko', 'w') as fileOut:
            with open('../data/generatedNduko') as fileIn:
                for line in range(self.n**6):
                    line = ['-' for i in range((self.n**4)*4)]
                    cell, row, column = fileIn.readline()[:-1].split()
                    line[int(cell)] = '1'
                    line[int(row)] = '1'
                    line[int(column)] = '1'
                    fileOut.write(''.join(line) + '\n')

if __name__ == '__main__':
    g = GenerateNduko(3)
    g.writeViewable()

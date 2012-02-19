#!/usr/bin/env python

class GenerateNduko(object):
    def __init__(self, n):
        self.n = n
        self.output = open('../data/nduko', 'w')

        cellValue = 0
        rowOffset = 0

        x, minx, bi, bj = 0, 0, 1, 1

        for i in range(n**4):
            for j in range(n**2):
                self.output.write('{0} {1} {2} {3}\n'.format(cellValue,
                                                     n**4 + (rowOffset * n**2 + (j % n**2)),
                                                     2*(n**4) + (n*i % n**3)*n + j,
                                                     3*(n**4) + x*n**2 + j))
            cellValue += 1
            if (i+1) % (n**2) == 0:
                rowOffset += 1

            if not bi % n:
                x += 1
                if not x % n:
                    x = minx
                    bj += 1
                    if not bj % n:
                        minx += n
            bi += 1

        self.output.close()

    def writeViewable(self):
        s = self.n**4
        with open('../data/viewableNduko', 'w') as fileOut:
            with open('../data/nduko') as fileIn:
                for line in range(self.n**6):
                    line = ['-' for i in range((self.n**4)*4)]
                    cell, row, column, block = fileIn.readline()[:-1].split()
                    line[int(cell)] = '1'
                    line[int(row)] = '1'
                    line[int(column)] = '1'
                    line[int(block)] = '1'
                    line = ''.join(line)
                    fileOut.write(line[:s] + '|' + 
                                  line[s:2*s] + '|' +
                                  line[2*s:3*s] + '|' +
                                  line[3*s:] +'\n')

if __name__ == '__main__':
    g = GenerateNduko(2)
    g.writeViewable()

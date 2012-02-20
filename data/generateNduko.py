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
                                                        n**4  + (rowOffset * n**2 + (j % n**2)),
                                                     2*(n**4) + (n*i % n**3)*n    +  j,
                                                     3*(n**4) +  x*n**2           +  j))
            if (i+1) % (n**2) == 0:
                rowOffset += 1

            if not bi % n:
                x += 1
                if not x % n:
                    x = minx
                    bj += 1
                    if not bj % n:
                        minx += n
            cellValue += 1
            bi += 1

        self.output.close()

    def writeViewable(self):
        s = self.n**4
        n = 0
        _r, _c = 1, 1
        with open('../data/viewableNduko', 'w') as fileOut:
            with open('../data/nduko') as fileIn:
                for line in range(self.n**6):
                    c = str(n % self.n**2 + 1)
                    line = ['-' for i in range((self.n**4)*4)]
                    cell, row, column, block = fileIn.readline()[:-1].split()
                    line[int(cell)] = c
                    line[int(row)] = c
                    line[int(column)] = c
                    line[int(block)] = c
                    line = ''.join(line)
                    fileOut.write('r{0}c{1}#{2} '.format(_r, _c, c) +
                                  line[:s] + '|' + 
                                  line[s:2*s] + '|' +
                                  line[2*s:3*s] + '|' +
                                  line[3*s:] +'\n')
                    n += 1
                    if not n % self.n**2:
                        if not _c % self.n**2:
                            _c = 0
                            _r += 1
                        _c += 1

if __name__ == '__main__':
    g = GenerateNduko(2)
    g.writeViewable()

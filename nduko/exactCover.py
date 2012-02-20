#!/usr/bin/env python

class ExactCover(object):
    def __init__(self):
        self._matrix = []
        self._solution = {}
        # self.coveredColumns = {}
        self._updates = {}

    def __str__(self):
        value = ' '.join(str(self._solution[k]-1) for k in self._solution)
        print self._updates
        return value

    def load(self, filename):
        '''Read in a matrix reperesenting the exact cover problem'''
        with open(filename,"r") as f:
            self._matrix = []
            row = 0
            for line in f:
                row = row + 1
                for col in line.split():
                    self._matrix.append((row, int(col)))

    def __chooseColumn(self, columns):
        '''Return the column with the smallest number of rows which is uncoverd'''
        columns = [c for c in columns if not columns[c]]

        # columns may possibly have no rows
        tmp = dict([(c, 0) for c in columns])
        for (r, c) in self._matrix:
            if c in columns:
                tmp[c] = tmp[c] + 1

        minColumn = columns[0]
        for c in columns:
            if tmp[c] < tmp[minColumn]:
                minColumn = c
        return minColumn

    def solve(self, k=0, columns={}, rows={}):
        '''Solve the exact cover problem'''
        if not columns:
            coveredColumns = {}
            for (r, c) in self._matrix:
                coveredColumns[c] = False
        else:
            coveredColumns = columns

        if not rows:
            coveredRows = {}
            for (r, c) in self._matrix:
                coveredRows[r] = False
        else:
            coveredRows = columns

        #If the matrix is empty, the problem is solved; terminate
        #successfully.
        if not self._matrix:
            for c in coveredColumns:
                if not coveredColumns[c]:
                    return False
            print self
            return False

        else:
            #otherwise choose a column c (deterministically)
            c = self.__chooseColumn(coveredColumns)
            print c
            # if 1 not in c:
            #     return False
            #choose a row r such that matrix(r, c) = 1
            rows = [node[0] for node in self._matrix if node[1]==c]
            if not rows:
                return False

            for r in rows:
                box = [] #a place for temporaly removed rows
                #include row r in the partial solution, if a solution
                #exists.
                solution = [node for node in self._matrix if node[0] == r]
                self._solution[k] = solution[1][1]
                # Remove row r from matrix.
                for node in solution:
                    box.append(node)
                    self._matrix.remove(node)
                    self._updates[k] = self._updates.get(k,0) + 1
                
                #For each column j such that matrix(r, j) = 1,
                cols = [node[1] for node in solution]
                for j in cols:
                    coveredColumns[j] = True
                    #choose rows i such that matrix(i,j) = 1.
                    rows2 = [node[0] for node in self._matrix if node[1] == j]
                    #delete row i from matrix
                    tmp = [node for node in self._matrix if node[0] in rows2]
                    for node in tmp:
                        box.append(node)
                        self._matrix.remove(node)
                        self._updates[k] = self._updates.get(k,0) + 1

                #do some recursion
                if self.solve(k + 1, coveredColumns, coveredRows):
                    #if this returns true, we have a solution, so terminate successfully
                    return True

                #restore deleted rows.
                for node in box:
                    self._matrix.append(node)
                del box
                del self._solution[k]
                #uncover columns.
                for j in cols:
                    coveredColumns[j] = False
        return True

if __name__ == '__main__':
    X = ExactCover()
    X.load('../data/nduko')
    try:
        print X.solve()
    except RuntimeError:
        print 'cannot solve'

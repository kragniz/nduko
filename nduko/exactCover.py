#!/usr/bin/python -O
#import pprint as pp

class ExactCover(object):
    def __init__(self):
        self._matrix = []
        self.solution = {}
        self.coveredColumns = {}
        self.updates = {}

    def __str__(self):
        print self.solution, self.updates, self.coveredColumns, self._matrix
        value = ' '.join(str(self.updates[k]-1) for k in self.updates)
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

        for (r, c) in self._matrix:
            self.coveredColumns[c] = False

    def __chooseColumn(self):
        """Return the column with the smallest number of rows which is uncoverd"""
        columns = [c for c in self.coveredColumns if not self.coveredColumns[c]]

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

    def solve(self, k):
        '''Solve the exact cover problem'''
        #If the matrix is empty, the problem is solved; terminate
        #successfully.
        if not self._matrix:
            for c in self.coveredColumns:
                if not self.coveredColumns[c]:
                    return True
            print self
            return True

        else:
            #otherwise choose a column c (deterministically)
            c = self.__chooseColumn()
            #choose a row r such that matrix(r, c) = 1
            rows = [node[0] for node in self._matrix if node[1]==c]
            if not rows:
                return False

            for r in rows:
                box = [] #a place for temporaly removed rows
                #include row r in the partial solution, if a solution
                #exists.
                solution = [node for node in self._matrix if node[0] == r]
                self.solution[k] = solution[1][1]
                # Remove row r from matrix.
                for node in solution:
                    box.append(node)
                    self._matrix.remove(node)
                    self.updates[k] = self.updates.get(k,0) + 1
                
                #For each column j such that matrix(r, j) = 1,
                cols = [node[1] for node in solution]
                for j in cols:
                    self.coveredColumns[j] = True
                    #choose rows i such that matrix(i,j) = 1.
                    rows2 = [node[0] for node in self._matrix if node[1] == j]
                    #delete row i from matrix
                    tmp = [node for node in self._matrix if node[0] in rows2]
                    for node in tmp:
                        box.append(node)
                        self._matrix.remove(node)
                        self.updates[k] = self.updates.get(k,0) + 1

                #do some recursion
                if self.solve(k + 1):
                    #if this returns true, we have a solution, so terminate successfully
                    return True

                #restore deleted rows.
                for node in box:
                    self._matrix.append(node)
                del box
                del self.solution[k]
                #uncover columns.
                for j in cols:
                    self.coveredColumns[j] = False
        return True

if __name__ == '__main__':
    X = ExactCover()
    X.load('../data/placement')
    try:
        X.solve(0)
    except RuntimeError:
        print 'cannot solve'

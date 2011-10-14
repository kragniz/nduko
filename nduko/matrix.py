class Matrix(object):
    def __init__(self):
        self.dataStructure = {}
        
    def setItem(self, r, c, value):
        try:
            self.dataStructure[c][r] = value 
        except KeyError:
            self.dataStructure[c] = {r:value}

    def getItem(self, r, c):
        return self.dataStructure[c][r]
        

if __name__ == '__main__':
    m = Matrix()
    #sets the item in row 0, column 0 to 1
    m.setItem(0, 0, 1)
    print m.getItem(0, 0)

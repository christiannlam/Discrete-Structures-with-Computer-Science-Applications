class Matrix:
    
    def __init__(self,rowsp):
        self.rowsp = rowsp
        colSpace = []
        self.colsp = colSpace
        l = len(rowsp[0])
        for i in range(l):
            col = []
            for row in rowsp:
                col.append(row[i])
            colSpace.append(col)
        return 
    
    def __add__(self, other):
        if((len(self.rowsp[0]) == len(other.rowsp[0])) & (len(self.colsp[0]) == len(other.colsp[0]))):
            add = []
            self.add = add
            l = len(self.colsp[0])
            m = len(self.rowsp[0])
            for i in range(l):
                a = []
                for j in range(m):
                    a.append(self.rowsp[i][j] + other.rowsp[i][j])
                add.append(a)
            return Matrix(add)
        
    def __sub__(self, other):
         if((len(self.rowsp[0]) == len(other.rowsp[0])) & (len(self.colsp[0]) == len(other.colsp[0]))):
            sub = []
            self.sub = sub
            l = len(self.colsp[0])
            m = len(self.rowsp[0])
            for i in range(l):
                s = []
                for j in range(m):
                    s.append(self.rowsp[i][j] - other.rowsp[i][j])
                sub.append(s)
            return sub
        
    def __mul__(self, other):  
        if type(other) == float:
            mult = []
            l = len(self.colsp[0])
            m = len(self.rowsp[0])
            for i in range(l):
                ml = []
                for j in range(m):
                    ml.append(self.rowsp[i][j] * other)
                mult.append(ml)
            return (Matrix(mult))
        elif type(other) == Matrix:
            if(len(self.colsp) == len(other.rowsp)):
                mat = []
                r = len(self.rowsp)
                c = len(other.rowsp[0])
                p = len(other.rowsp)
                total = 0
                for i in range(r):
                    mat2 = []
                    for j in range(c):
                        for k in range(p):
                            total += self.rowsp[i][k] * other.rowsp[k][j]
                        mat2.append(total)
                        total = 0
                    mat.append(mat2)
                return (Matrix(mat))
        elif type(other) == Vec:
            if(len(self.colsp) == len(other.elements)):
                vSize = len(self.rowsp)
                resultVec = []
                for i in range(vSize):
                    resultVec.append(0)
                j = 0
                for row in self.rowsp:
                    for i in range(len(self.colsp)):
                        resultVec[j] += row[i] * other.elements[i]
                    j = j + 1
                return (Vec(resultVec))
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other):  
        if type(other) == float:
            mult = []
            l = len(self.colsp[0])
            m = len(self.rowsp[0])
            for i in range(l):
                mult2 = []
                for j in range(m):
                    mult2.append(self.rowsp[i][j] * other)
                mult.append(mult2)
            return (Matrix(mult))
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __str__(self):
        for row in self.rowsp:
            for i in row:
                print(i, end = "\t")
            print(" ")
        return ""

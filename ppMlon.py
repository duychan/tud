import numpy as np
class ppMlon:
    def __init__(self, c, a, b):
        self.c = c.astype(np.float)
        self.a = a.astype(np.float)
        self.b = b.astype(np.float)
        self.num_x = self.a.shape[1]
        
    def init_table(self):
        self.anCoBan = np.arange(self.num_x, self.num_x + len(self.b)).astype(np.float)
        self.heSo = np.ones((len(self.b),), dtype = np.float) * 1000
        self.z = np.zeros(self.c.shape)
        for i in range(self.num_x):
            self.z[i] = np.sum(self.heSo * self.a[:,i]) - self.c[i]
            print(i)
    
    def best(self):
        return all(self.z <= 0)
    
    def unSolve(self):
        for i in range(self.num_x):
            if self.z[i] > 0 and all(self.a[:,i] <= 0):
                return True
        return False
    
    def nextTable(self):
        # find in
        index_in = np.argmax(self.z)
        # find out
        self.lamda = self.b / self.a[:,index_in]
        self.lamda = np.where(self.lamda <= 0, np.inf, self.lamda)
        index_out = np.argmin(self.lamda)
        # change out -> in
        self.anCoBan[index_out] = index_in
        self.heSo[index_out] = self.c[index_in]
        # change b & a
        self.b[index_out] = self.b[index_out] / self.a[index_out, index_in]
        self.a[index_out] = self.a[index_out] / self.a[index_out,index_in]
        for i in range(len(self.b)):
            if i != index_out:
                self.b[i] = self.b[i] - self.b[index_out] * self.a[i, index_in]
                self.a[i] = self.a[i] - self.a[index_out] * self.a[i,index_in]
        #calc z
        for i in range(self.num_x):
            self.z[i] = np.sum(self.heSo * self.a[:,i]) - self.c[i]           
    
    def printResult(self):
        print('Minimum = ', np.sum(self.heSo * self.b))
        for i in range(len(self.b)):
            if self.anCoBan[i] < self.num_x:
                print(f"x[{int(self.anCoBan[i])}] = {self.b[i]}")
                
    def run(self):
        self.init_table()
        while True:
            if self.best():
                self.printResult()
                return np.sum(self.heSo * self.b)
            elif self.unSolve():
                print("can't not solve")
            else:
                self.nextTable()
                
if __name__ == "__main__":
    c = np.array([3,-3,1,-1])
    a = np.array([
        [-1,1,2,1],
        [1,1,-1,-1],
        [3,2,-6,3]
    ])
    b = np.array([2,6,9])
    sm = ppMlon(c,a,b)
    sm.run()
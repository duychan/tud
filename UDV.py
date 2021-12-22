import numpy as np
def SapXep(e,v):
    
    return
def SVD(A, m, n):
    U = np.zeros((m, m), float)
    V = np.zeros((n, n), float)
    e, V = np.linalg.eig(np.dot(np.transpose(A), A))
    e = list(e)
    V = SapXep(e, V)
    D = np.zeros((m, n), float)
    temp = V.transpose()
    if n > m:
        for i in range(m):
            D[i][i] = np.sqrt(e[i])
        for i in range(m):
            U[i] = np.dot(np.array(A), np.array(temp[i])) / D[i][i]
        else:
            for i in range(n):
                D[i][i] = np.sqrt(e[i])
                for i in range(n):
                    U[i] = np.dot(np.array(A), np.array(temp[i])) / D[i][i]
                    U = np.transpose(U)
                    V = temp
    return U, D, V

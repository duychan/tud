import numpy as np
from numpy.linalg import eig
from math import sqrt

def NhapMatrix(A,m,n):
    for i in range(m):
        a =[]
        for j in range(n):
            a.append(int(input()))
        A.append(a)
    return A

def nhan(A,B,m,n,q):
    kq = np.zeros((m,q),float)

    for i in range(m):
        for j in range(q):
            for k in range(n):
                kq[i][j] += A[i][k] * B[k][j]
    return kq

def arrange(l,A):
    A = A.transpose()
    d = list(zip(l,A))
    l.sort(reverse=True)
    d.sort(key=lambda x: x[0],reverse=True)
    return np.array([i[1] for i in d]).transpose()

def SVD(A,m,n):
    U = np.zeros((m,m),float)
    VT = np.zeros((n,n),float)
    D = np.zeros((m,n),float)
    T = np.dot(AT,A)
    lamdaV,v = eig(T)
    lamdaV = list(lamdaV)
    v = arrange(lamdaV,v)
    VT = v.transpose()
    for i in range(m):
        for j in range(n):
            if i==j: D[i][j] = sqrt(lamdaV[i])
            else:continue
    if n > m:
        for i in  range(m):
            U[i] = (np.array(A) @ np.array(VT[i])) / D[i][i]
    else:
        for i in  range(n):
            U[i] = (np.array(A) @ np.array(VT[i])) / D[i][i]
    U = U.transpose()
    return U , D , VT

A = []
D = []
U = []
VT = []
m = int(input("Nhap vao so hang m : "))
n = int(input("Nhap vao so cot n : "))
NhapMatrix(A,m,n)
A = np.array(A)
AT = A.transpose();
print('--------Matrix A---------\n' + str(A) +'\n');
print('--------Matrix AT---------\n' + str(AT) +'\n');
U , D , VT = SVD(A,m,n)
print('----- Matrix U: -----\n' + str(U) + '\n')
print('----- Matrix D: -----\n' + str(D) + '\n')
print('----- Matrix VT: -----\n' + str(VT) + '\n')
UD = nhan(U,D,m,m,n)
print('----- Matrix U*D: -----\n' + str(UD) + '\n')
A2 = nhan(UD,VT,m,n,n)
print('-----Check Matrix A: -----\n' + str(A2) + '\n')
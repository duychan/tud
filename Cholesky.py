import numpy as np
import math

# kiểm tra ma trận đối xứng
def checkDoiXung(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
                if A[i][j] != A[j][i]:
                    return False
    return True

# kiểm tra ma trận xác định dương
def checkXDDuong(V):
    for x in V:
        if x <= 0:
            return False
    return True

# thực hiện kiểm tra
def matrix_can_use_cholesky(A):
    m, n = np.shape(A)
    if m != n: # kiểm tra ma trận vuông
        print(">> Ma tran A khong vuong !")
        return False
    if checkDoiXung(A) is False:
        print(">> Ma tran A khong doi xung !")
        return False
    V = np.linalg.eigvals(A)
    if not checkXDDuong(V):
        print(">> Ma tran A khong xac dinh duong !")
        return False
    return True

# phân rã ma trận
def Cholesky(matrix):
    matrix = np.array(matrix,float)
    L = np.zeros_like(matrix)
    n,_ = np.shape(matrix)

    for j in range(n):
        for i in range(j,n):
            sum1 = 0;
            if ( j == i):
                for k in range(j):
                    sum1 += pow(L[j][k], 2);
                L[j][i] = math.sqrt(matrix[j][i] - sum1);
            else:

                for k in range(j):
                    sum1 += (L[i][k] * L[j][k]);
                if (L[j][j] > 0):
                    L[i][j] = (matrix[i][j] - sum1) / L[j][j];
    A = np.dot(L,np.transpose(L))
    print('--------Matrix A---------\n' + str(A) +'\n');
    print('--------Result---------\n' + str(L) +'\n');
    
n=3;
A = [[7.3,1,0],
    [1,20,3.5],
    [0,3.5,2]];
if matrix_can_use_cholesky(A):
    Cholesky(A)
else:
    print("Ma tran A khong du dieu kien phan ra Cholesky")

    
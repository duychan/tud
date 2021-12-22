import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)

def cost(w):
    N = Xbar.shape[0]
    return 0.5/N*np.linalg.norm(y - Xbar.dot(w), 2)**2;

def myGD(w_init,grad,alpha,loop=100,esilon=1e-4):
    w = [w_init]
    for i in range(loop):
        w_new = w[-1] - alpha*grad(w[-1])
        if np.linalg.norm(grad(w_new))/len(w_new) < esilon:
            break
        w.append(w_new)
    return(w,i)


X = np.random.rand(1000,1)
y = 4 + 3 * X + .2*np.random.randn(1000, 1)

one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one, X), axis = 1)

w_init = np.array([[2],[1]])
(w1,it1) = myGD(w_init,grad,1)
print(' Phương pháp GradientDescent: w = ', w1[-1].T, ',\n after %d iterations.' %(it1+1))

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w_lr = np.dot(np.linalg.pinv(A), b)
print('Solution found by formula: w = ',w_lr.T)

w = w_lr
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0, 1, 2, endpoint=True)
y0 = w_0 + w_1*x0

plt.plot(X.T, y.T, 'b.')
plt.plot(x0, y0, 'y', linewidth = 2)
plt.axis([0, 1, 0, 10])
plt.show()
import numpy as np
def grad(x):
 return (8/np.exp(2*x) - 4/np.exp(x))
def cost(x):
 return pow(1-2/np.exp(x),2)
def myGD1(eta, x0):
 x = [x0]
 for it in range(100):
    x_new = x[-1] - eta*grad(x[-1])
    if abs(grad(x_new)) < 1e-3:
        break
 x.append(x_new)
 return (x, it)
if __name__ == '__main__':
 (x1, it1) = myGD1(0.1, -1)
 (x2, it2) = myGD1(0.1, 1)
 print('Solution x1 = %f, cost = %f, obtained after %d iterations'%(x1[-1], cost(x1[-1]), it1))
 print('Solution x2 = %f, cost = %f, obtained after %d iterations'%(x2[-1], cost(x2[-1]), it2))
import numpy as np
# f(x)
def cost(x):
 return (np.exp(-x) - 2/np.exp(x))**2
# f'(x)
def grad(x):
 return -2*np.exp(-2*x)
def myGD(alpha, x0, gra=1e-3, loop=1000):
 x = [x0]
 for i in range(loop):
    x_new = x[-1] - alpha*grad(x[-1])
    if abs(grad(x_new)) < gra:
        break
 x.append(x_new)
 return (x, i)
if __name__ == "__main__":
 (x1, it1) = myGD(.1, 0.2)
 (x2, it2) = myGD(.1, 0.3)
 print('Solution x1 = %f, cost = %f, obtained after %d iterations' %(x1[-1], cost(x1[-1]), it1))
 print('Solution x2 = %f, cost = %f, obtained after %d iterations' %(x2[-1], cost(x2[-1]), it2))
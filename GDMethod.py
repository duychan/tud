import math
import numpy as np
import math
import matplotlib.pyplot as plt


def cost(x):
    return (1-2/np.exp(x))**2


def grad(x):
    return 4/math.exp(x)*(1-2/math.exp(x))


def GD(alpha, x0, gra=1e-3, loop=1000):
    x = x0
    for i in range(loop):
        x = x - alpha*grad(x)
        if abs(grad(x)) < gra:
            break
    return (x, i)


if __name__ == '__main__':
    X = np.linspace(-5, 5, 500)
    y = cost(X)
    plt.plot(X.T, y.T, 'b.')
    plt.axis([-5, 5, -5, 20])
    (x, it) = GD(0.1, 0.01)

    print("x =", x, "cost = ", cost(x), "obtained after", it, "iterations")

    plt.plot(x, cost(x), 'rX')

    plt.show()

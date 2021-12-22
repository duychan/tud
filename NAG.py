import numpy as np
import matplotlib.pyplot as plt

def grad(x):
    return 2*x+ 10*np.cos(x)

def cost(x):
    return x**2 + 10*np.sin(x)

def GD_momentum(theta_init, alpha=0.1, beta=0.9, Loop = 1000):
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)

    for it in range(Loop):
        v_new = beta*v_old + alpha*grad(theta[-1] - beta * v_old)
        theta_new = theta[-1] - v_new
        theta.append(theta_new)
        v_old = v_new
    return (theta,it)

if __name__ == '__main__':
    X = np.linspace(-5, 5, 200)
    y = cost(X)
    plt.plot(X.T, y.T, 'r.')
    plt.axis([-5, 5, -10, 15])
    (x, it) = GD_momentum(5, 0.1, beta=0.9)
    print('Momentum_Solution x = %f, cost = %f, obtained after %d iterations'%(x[-1], cost(x[-1]), it))
    plt.plot(x[-1], cost(x[-1]), 'b X')
    plt.show()



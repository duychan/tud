import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)

def sgrad(w, i, rd_id):
    true_i = rd_id[i]
    xi = Xbar[true_i, :]
    yi = y[true_i]
    a = np.dot(xi, w) - yi
    return (xi*a).reshape(2, 1)

def l(w):
    N = Xbar.shape[0]
    return .5 / N*np.linalg.norm(Xbar.dot(w)-y, 2)**2

def SGD(w_init, grad, eta):
    w = [w_init]
    w_last_check = w_init
    iter_check_w = 10
    N = X.shape[0]
    count = 0
    for it in range(10):
        # shuffle data 
        rd_id = np.random.permutation(N)
        for i in range(N):
            count += 1 
            g = sgrad(w[-1], i, rd_id)
            w_new = w[-1] - eta*g
            w.append(w_new)
            if count%iter_check_w == 0:
                w_this_check = w_new                 
                if np.linalg.norm(w_this_check - w_last_check)/len(w_init) < 1e-3:                                    
                    return w
                w_last_check = w_this_check
    return w

if __name__ == '__main__':
    # dataset
    X = np.random.rand(1000, 1)
    y = 4 + 3 * X + .2 * np.random.randn(1000, 1)  # noise added
    # Building Xbar
    one = np.ones((X.shape[0], 1))
    Xbar = np.concatenate((one, X), axis=1)
    # Gradient descent
    w_init = np.array([[2], [1]])
    w1 = SGD(w_init, sgrad, 0.01)
    print(f'Phương pháp GradientDescent: w = {w1[-1].T},\nl = {l(w1[-1])}')

    #Display result
    #w = w_lr
    w = w1[-1]
    w_0 = w[0][0]
    w_1 = w[1][0]
    x0 = np.linspace(0, 1, 2, endpoint=True)
    y0 = w_0 + w_1 * x0

    # Draw the fitting line
    plt.plot(X.T, y.T, 'b.')  # data
    plt.plot(x0, y0, 'y', linewidth=2)  # the fitting line
    plt.axis([0, 1, 0, 10])
    plt.show()
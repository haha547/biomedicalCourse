import numpy as np
def computeCostMulti(X, y, theta):
    
    # Initialize some useful values
    m = len(y) # number of training examples

    error = np.dot(X, theta) - y
    J = np.dot(error.T, error) /m/2
    print(J)
    return J

def gradientDescentMulti(X, y, theta, alpha, num_iters):
    
    # Initialize some useful values
    m = len(y) # number of training examples
    J_history = np.zeros((num_iters, 1))

    for iter in range(num_iters):
        print("step:", iter)
        error = np.dot(X,theta) - y
        theta = theta - alpha * np.dot(X.T,error) / m

        J_history[iter][0] = computeCostMulti(X, y, theta)

    return theta, J_history
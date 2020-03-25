"""
def featureNormalize(X):
    
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    #(X-mu)/sigma   回傳標準化後的陣列
    #mu             回傳每個行的平均值
    #sigma          回傳每個行的標準差
    return (X-mu)/sigma, mu, sigma

def computeCostMulti(X, y, theta):
    
    # Initialize some useful values
    m = len(y) # number of training examples

    error = np.dot(X,theta) - y
    J = np.dot(error.T, error) /m/2

    return J

def gradientDescentMulti(X, y, theta, alpha, num_iters):
    
    # Initialize some useful values
    m = len(y) # number of training examples
    J_history = np.zeros((num_iters, 1))

    for iter in range(num_iters):

        error = np.dot(X,theta) - y
        theta = theta - alpha * np.dot(X.T,error) / m

        J_history[iter][0] = computeCostMulti(X, y, theta)

    return theta, J_history
"""
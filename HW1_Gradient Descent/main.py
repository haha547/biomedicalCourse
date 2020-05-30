import pandas as pd
import numpy as np
from libary import gradientDescentMulti, computeCostMulti
df = pd.read_csv("/Users/xuhaozhe/Desktop/AIinBiomedical/HW1_Gradient Descent/train.csv")
data = df.to_numpy()
data = np.delete(data, [0,1,2], axis=1)
data = np.split(data, 240, axis=0)
for i in range(239):
    data[0] = np.concatenate((data[0],data[i+1]), axis = 1)
Y = data[0][9][9:].reshape(-1, 1)
m = len(Y)
X = data[0]
#X = np.vstack((np.ones(m), X))
learning_rate = 0.001
num_iter = 100000
print("y.s", Y.shape)
print("x.s", X.shape)
a = np.ones((162,1))
for i in range(5751):
    a= np.hstack((a, X.T[i:i+9].reshape(-1,1)))
a = np.delete(a,[0], axis =1)
a = np.vstack((a, np.ones((5751))))
theta = np.zeros((163,1))
theta, J_history = gradientDescentMulti(a.T, Y, theta, learning_rate, num_iter)
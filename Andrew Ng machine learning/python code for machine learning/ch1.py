import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = "E:\python程序练习\machine learning\machine-learning-ex1\ex1"
data = pd.read_csv(path + "\ex1data1.txt", header=None,
                   names=("Population", "Profit"))

# data.plot(kind="scatter", x="Population", y="Profit")

# 定义一个计算cost function的函数


def costfunction(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    cost = np.sum(inner) / (2 * len(X))
    return(cost)

data.insert(0, "ones", 1)  # 在第一列加上1，变为设计矩阵形式

X = data.ix[:, 0:2]
y = data.ix[:, 2:3]

X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0, 0]))

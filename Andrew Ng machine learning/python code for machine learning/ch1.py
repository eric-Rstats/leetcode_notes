import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
path = "E:\python学习\吴恩达机器学习\machine-learning-ex1\ex1"
data = pd.read_csv(path + "\ex1data1.txt", header=None,
                   names=("Population", "Profit"))
data2 = pd.read_csv(path + "\ex1data2.txt", header=None, names=['Size', 'Bedrooms', 'Price'])
# data.plot(kind="scatter", x="Population", y="Profit")

# 定义一个计算cost function的函数
def costfunction(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    cost = np.sum(inner) / (2 * len(X))
    return(cost)

data.insert(0, "ones", 1)  # 在第一列加上1，变为设计矩阵形式

X = data.iloc[:, 0:2]
y = data.iloc[:, 2:3]

X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0, 0]))
costfunction(X, y, theta)

def gradient1(X, y, theta, alpha, iter):
    p = X.shape[1] #feature个数为p-1个
    cost = np.zeros(iter)
    tmp = np.matrix(np.zeros(theta.shape))
    for i in range(iter):
        error = X * theta.T - y

        for j in range(p):
            term = np.multiply(error, X[:,j])
            tmp[0,j] = theta[0,j] - ((alpha / len(X)) * np.sum(term))

        theta = tmp
        cost[i] = costfunction(X,y,theta)
    return theta, cost


# 使用sklearn对数据data2进行多元线性回归
x2 = data2.iloc[:,0:2]
y2 = data2.Price
reg2 = linear_model.LinearRegression(normalize=True)
reg2.fit(x2,y2)

print("这个多元线性回归的系数是: %.3f" % reg2.intercept_, reg2.coef_)

# 使用sklearn对数据data1进行多元线性回归
reg1 = linear_model.LinearRegression()
reg1.fit(X,y)

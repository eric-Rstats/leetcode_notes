# -*- coding=utf-8 -*-
# chapter 3 classification

# fetch the MNIST 数据集
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')

import matplotlib.pyplot as plt
import matplotlib
import numpy as np 

X = mnist.data
y = mnist.target
random_pic = np.random.randint(0, 10000)
random_pic_image = X[random_pic].reshape(28,28)
plt.imshow(random_pic_image, cmap=matplotlib.cm.binary,
           interpolation='nearest')
           
# 尝试重现书本上的，从0到9依次绘图的大图
for i in range(10):
    pic = X[y==i][:10]
    for j in range(10):
        plt.subplot(10,10,10*i+(j+1))
        plt.imshow(pic[j].reshape(28,28))
        plt.axis('off')

# 随机打乱数据
X_train, y_train, X_test, y_test = X[:60000], y[:60000], X[60000:],y[60000:]

# random_shuffle
random_ix = np.random.permutation(60000)
X_train, y_train = X_train[random_ix], y_train[random_ix]


# 首先考虑一个二分类问题，书中考虑的是是不是0
y_train_0 = (y_train==0)
y_test_0 = (y_test==0)

#  使用SGD进行二分类的训练
from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=129)
sgd_clf.fit(X_train, y_train_0)

sgd_clf.predict(X[random_pic])  # 输出为True,是0

# evaluate the model performance
from sklearn.model_selection import cross_val_predict
y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_0, cv=3)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_train_0, y_train_pred)

from sklearn.metrics import precision_score, recall_score, f1_score
precision_score(y_train_0, y_train_pred)
recall_score(y_train_0, y_train_pred)
f1_score(y_train_0, y_train_pred)

# precision/recall tradeoff

y_scores = cross_val_predict(sgd_clf, X_train, y_train_0, 
                             cv=3,method='decision_function')
from sklearn.metrics import precision_recall_curve
precision, recall, threshold = precision_recall_curve(y_train_0, y_scores)

def plot_precision_recall_vs_threshold(precision, recall, threshold):
    plt.plot(threshold, precision[:-1], 'b--', label='Precision')
    plt.plot(threshold, recall[:-1], 'g--', label='Recall')
    plt.xlabel('Threshold')
    plt.ylim([0,1])
    plt.legend(loc='best')

plot_precision_recall_vs_threshold(precision, recall, threshold)

# ROC CURVE
from sklearn.metrics import roc_curve
fpr, tpr, threshold = roc_curve(y_train_0, y_scores)

def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr,tpr,linewidth=2,label=label)
    plt.plot([0,1],[0,1],'k--')
    plt.axis([0,1,0,1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

plot_roc_curve(fpr,tpr)

# 计算AUC的值
from sklearn.metrics import roc_auc_score
roc_auc_score(y_train_0, y_scores)

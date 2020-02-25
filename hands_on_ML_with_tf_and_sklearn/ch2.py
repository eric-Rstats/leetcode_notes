# -*- coding: UTF-8 -*-

import os
import tarfile
from six.moves import urllib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 下载数据
DOWNLOAD_ROOT = 'https://raw.githubusercontent.com/ageron/handson-ml/master/'
HOUSING_PATH = 'datasets/housing'
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + '/housing.tgz'


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    """
    定义函数获取第一章中，房价预测的数据

    parameters:
    -------
    housing_url: url地址
    housing_path: 数据存储位置
    """
    if not os.path.isdir(housing_path):
        # 如果目录不存在，新建目录
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, 'housing.tgz')
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    """
    下载数据后，从目录中载入数据
    """
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)


fetch_housing_data()
housing = load_housing_data()
print '载入数据成功, 数据shape为: %d,%d \n' % (housing.shape)

# 选取一部分数据作为测试集


def split_train_test(data, test_ratio):
    """
    训练集、测试集的划分l
    parameter
    ----
    data: 数据集
    test_ratio: 测试集的比例

    return
    ---
    二元元组：训练集与测试集
    """
    # 利用permutation对索引进行打乱
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


print '对原数据进行训练集与测试集的划分，请输入测试集的比例(0~1)：\n'
test_ratio = input()

print '进行训练集与测试集的划分，训练集比例为 %d%% ， 测试集的比例: %d%%' % ((1 - test_ratio) * 100, test_ratio * 100)

train_set, test_set = split_train_test(housing, test_ratio)
print '划分成功\n'

# 对收入进行划分，考虑分层抽样
housing['income_cat'] = np.ceil(housing['median_income'] / 1.5)
housing['income_cat'].where(housing['income_cat'] < 5, 5.0, inplace=True)

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing['income_cat']):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# 移除strat数据中的cat列
for set in (strat_train_set, strat_test_set):
    set.drop(['income_cat'], axis=1, inplace=True)

# Discover and visualize the data
data = strat_train_set.copy()
data.plot(kind='scatter', x='longitude', y='latitude', alpha=0.4,
          s=housing['population'] / 100, label='population', figsize=(10, 7),
          c='median_house_value', cmap=plt.get_cmap('jet'), colorbar=True,)

# 从这张图中可以发现人口，价格与坐标有关系
# looking for correlation
corr_matrix = data.corr()
# 可以看出收入与房屋价格相关系数很高

# attributes
data['rooms_per_household'] = data['total_rooms'] / \
    data['households']  # 平均每家的卧室数量
data['bedrooms_per_room'] = data['total_bedrooms'] / data['total_rooms']
data['populatoin_per_household'] = data['population'] / housing['households']

# Data cleaning
# 考虑将特征与label分开，对x进行特征上的transformation或者combination，
# 同时这些清洗过程，最好写成函数形式，方便之后调用
# 注： drop是一种copy方法

housing = strat_train_set.drop('median_house_value', axis=1)
housing_label = strat_train_set['median_house_value'].copy()

# total_bedrooms这列有一些缺失值
# sklearn中的缺失值处理函数
from sklearn.preprocessing import Imputer
imputer = Imputer(strategy="median")  # 定义使用中位数来做缺失值填充

# 由于只有数值型情况下才可以使用缺失值填充，因此要保证数据都是数值型的
housing_num = housing.drop('ocean_proximity', axis=1)
imputer.fit(housing_num)
X = imputer.transform(housing_num)  #  返回的是一个numpy对象
housing_tr = pd.DataFrame(X, columns=housing_num.columns)

# Text and categorical attributes
# ocean_proximity是一个类似factor的object
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
encoder = LabelEncoder()
housing_cat = housing['ocean_proximity']
housing_cat_encoded = encoder.fit_transform(housing_cat)

print encoder.classes_

# 更好地是使用one-hot-encoding
encoder = OneHotEncoder()
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1, 1))
# 以上返回的是一个scipy的稀疏矩阵

# 一步到位将text 变量转化为热编码形式
from sklearn.preprocessing import Binarizer
encoder = Binarizer()
housing_cat_1hot = encoder.fit_transform(housing_cat)

# ---------------------------------------------------
#             自定义transformer                      #
#---------------------------------------------------#
from sklearn.base import BaseEstimator, TransformerMixin
rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
        population_per_household = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


attr_adder = CombinedAttributesAdder(add_bedrooms_per_room=False)
housing_extra_attribs = attr_adder.transform(housing.values)

#-------------------------------------------------#
#             feature scaling                     #
# 由于变量之间不同的量纲，可能给模型带来巨大的影响
#-------------------------------------------------#
# 使用sklearn提供的transformer的pipeline

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# a pipeline constructor
num_pipeline = Pipeline([
    ('imputer', Imputer(strategy="median")),
    ('attr_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
])

housing_num_tr = num_pipeline.fit_transform(housing_num)

# 将数值型与字符型转换一体化

from sklearn.pipeline import FeatureUnion
from utils import CategoricalEncoder # 从自定义文件中引入新定义的categoricalencoder

num_attribs = list(housing_num) # pd.DataFrame -> 包含列名的列表
cat_attribs = ['ocean_proximity']

class DataFrameSelector(BaseEstimator, TransformerMixin):
    """
    此class是为了将pandas对象转化为ndarray，根据列名选取所需要的列
    """
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values

num_pipeline = Pipeline([
    ('selector', DataFrameSelector(num_attribs)),
    ('imputer', Imputer(strategy="median")),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),
])

cat_pipeline = Pipeline([
    ('selector', DataFrameSelector(cat_attribs)),
    ('label_binarizer', CategoricalEncoder(encoding='onehot-dense')),
])

full_pipeline = FeatureUnion(transformer_list=[
    ('num_pipeline', num_pipeline),
    ('cat_pipeline', cat_pipeline),
])

housing_prepared = full_pipeline.fit_transform(housing)

# 注意上述过程后，返回的是一个ndarray


#--------------------------------------#
#            训练模型                    #
#---------------------------------------#
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_label)

print lin_reg.score(housing_prepared, housing_label)

from sklearn.metrics import mean_squared_error
housing_predictions = lin_reg.predict(housing_prepared)
lin_rmse = np.sqrt(mean_squared_error(housing_predictions, housing_label))


# 决策树
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(housing_prepared, housing_label)
housing_predictions = tree_reg.predict(housing_prepared)
tree_rmse = np.sqrt(mean_squared_error(housing_predictions, housing_label))
print tree_rmse

#---------------------------------#
#          cross validation       #
#---------------------------------#
from sklearn.model_selection import cross_val_score
scores = cross_val_score(tree_reg, housing_prepared, housing_label, 
                         scoring='neg_mean_squared_error', cv=10)
# 返回的是负数
rmse_scores = np.sqrt(-scores)

lin_scores = cross_val_score(lin_reg, housing_prepared, housing_label,
                             scoring='neg_mean_squared_error', cv=10)
lin_rmse_scores = np.sqrt(-lin_scores)

# 随机森林
from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor()
#forest_reg.fit(housing_prepared, housing_label)
forest_scores = cross_val_score(forest_reg, housing_prepared, housing_label,
                                scoring='neg_mean_squared_error', cv=10)
forest_rmse = np.sqrt(-forest_scores)        


#--------------------------------#
#         fine-tune              #
#--------------------------------#
from sklearn.model_selection import GridSearchCV
param_grid = [
    {'n_estimators':[3,10,30], 'max_features':[2,4,6,8]},
    {'bootstrap':[False], 'n_estimators':[3,10],'max_features':[2,3,4]},
]
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
                           scoring='neg_mean_squared_error') 
grid_search.fit(housing_prepared, housing_label)               

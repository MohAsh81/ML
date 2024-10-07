from sklearn.linear_model import Ridge
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('./Melbourne_housing_FULL.csv')

cols_to_use = ['Suburb', 'Rooms', 'Type', 'Method', 'SellerG', 'Regionname', 'Propertycount',
               'Distance', 'CouncilArea', 'Bedroom2', 'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'Price']
dataset = dataset[cols_to_use]


cols_to_fill_zero = ['Propertycount',
                     'Distance', 'Bedroom2', 'Bathroom', 'Car']
dataset[cols_to_fill_zero] = dataset[cols_to_fill_zero].fillna(0)


dataset['Landsize'] = dataset['Landsize'].fillna(dataset.Landsize.mean())
dataset['BuildingArea'] = dataset['BuildingArea'].fillna(
    dataset.BuildingArea.mean())


dataset.dropna(inplace=True)

dataset = pd.get_dummies(dataset, drop_first=True)

X = dataset.drop('Price', axis=1)
y = dataset['Price']


train_X, test_X, train_y, test_y = train_test_split(
    X, y, test_size=0.3, random_state=2)


# reg = LinearRegression().fit(train_X, train_y)
# print(reg.score(test_X, test_y))

lasso_reg = linear_model.Lasso(alpha=50, max_iter=100, tol=0.1)
lasso_reg.fit(train_X, train_y)

print(lasso_reg.score(test_X, test_y))

ridge_reg = Ridge(alpha=50, max_iter=100, tol=0.1)
ridge_reg.fit(train_X, train_y)

print(ridge_reg.score(test_X,test_y))

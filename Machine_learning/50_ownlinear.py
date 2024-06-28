import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

x,y =load_diabetes(return_X_y=True)

class meralr:
    def __init__(self):
        self.coeff=None
        self.intercept=None
    def fit(self ,x_train,y_train):
        x_train=np.insert(x_train,0,1,axis=1)
        print(x_train.shape)
        betas=np.linalg.inv(np.dot(x_train.T,x_train)).dot(x_train.T).dot(y_train)
        self.intercept=betas[0]
        self.coeff=betas[1:]
        print(self.intercept)
        print(self.coeff)
        print(self.coeff.shape)
        
    def predict(self,x_test):
        y_pred=self.intercept+np.dot(x_test,self.coeff.reshape(10,1))
        return y_pred

clf=meralr()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=2)
clf.fit(x_train,y_train)
print(x_train.shape)
y_pred=clf.predict(x_test)
print(r2_score(y_test,y_pred))
print(mean_squared_error(y_test,y_pred))
print(mean_absolute_error(y_test,y_pred))
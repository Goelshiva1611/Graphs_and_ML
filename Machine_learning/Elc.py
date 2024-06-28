import matplotlib.pyplot as plt
import pandas as pd
import numpy as py
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
df=pd.read_csv("data (1).csv")
# print(df.head())
print(df.shape)
# print(df.describe())

# Train and Test split of the data should be in the ratio of 60:40, 70:30, 75:25,
# 80:20, 90:10, 95:5.
y=df.iloc[:,0:1].values
x=df.iloc[:,1:].values

x_train1,x_test1,y_train1,y_test1=train_test_split(x,y.ravel(),test_size=0.4,random_state=2)
x_train2,x_test2,y_train2,y_test2=train_test_split(x,y.ravel(),test_size=0.3,random_state=2)
x_train3,x_test3,y_train3,y_test3=train_test_split(x,y.ravel(),test_size=0.25,random_state=40)
x_train4,x_test4,y_train4,y_test4=train_test_split(x,y.ravel(),test_size=0.2,random_state=2)
x_train5,x_test5,y_train5,y_test5=train_test_split(x,y.ravel(),test_size=0.1,random_state=2)
x_train6,x_test6,y_train6,y_test6=train_test_split(x,y.ravel(),test_size=0.05,random_state=2)

df1=pd.read_csv("test.csv")
test_case=df1.iloc[:,0:]
clf=KNeighborsClassifier(n_neighbors=10)
clf.fit(x_train1,y_train1)
y_pred=clf.predict(x_test1)
y_testcase=clf.predict(test_case)
print(y_pred)
print(y_test1)
print(accuracy_score(y_test1,y_pred))
print(y_testcase)
print(x_train1.shape)
# y_1=clf.predict(df1)
# print(y_1)

print(df1.shape)
print(classification_report(y_test1,y_pred))
print(confusion_matrix(y_test1, y_pred))
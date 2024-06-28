import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

class MeraLr:
    def __init__(self) :
        self.m=None
        self.b=None
    def fit(self,x_train,y_train) : 
        num=0
        den=0
        for i in range(x_train.shape[0]):
            num=num+((x_train[i]-x_train.mean())*(y_train[i]-y_train.mean()))
            den=den+((x_train[i]-x_train.mean())*(x_train[i]-x_train.mean()))
        
        self.m=num/den
        self.b=y_train.mean()-(self.m*x_train.mean())
        print(self.m)
        print(self.b)
    def predict(self,x_test):
        
        return (self.m*x_test )+ self.b



df=pd.read_csv('placement.csv')
print(df.head())

x=df.iloc[:,0:1].values
y=df.iloc[:,-1].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

print(x_test[0])

clf=MeraLr()
clf.fit(x_train,y_train)

print(clf.predict(x_test[0]))

# Plotting the results
plt.scatter(df['cgpa'], df['package'], color='blue', label='Actual Data',marker="+")
plt.plot(x_train, clf.predict(x_train), color='red', linewidth=2, label='Regression Line')
plt.xlabel("CGPA")
plt.ylabel("Package")
plt.title("CGPA vs Package with Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

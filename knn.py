import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
from sklearn.metrics import r2_score
from sklearn.datasets import load_iris
from sklearn.metrics import recall_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
x,y=load_iris(return_X_y=True)
print(x)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=13)

k=np.sqrt(x.shape[0])
print(k)
accuracy=[]
for i in range(1,26):
    k=i
    clf=KNeighborsClassifier(n_neighbors=k)
    clf.fit(x_train,y_train)
    y_pred=clf.predict(x_test)
    accuracy.append(accuracy_score(y_test,y_pred))
plt.plot(range(1,26),
         accuracy,
         color="blue",
         alpha=0.40,
         linewidth=1.5,
         marker='o',
         linestyle="solid",
         label='Actual Data'
         )
plt.grid()
plt.title("Graph to find k nearest neighbours .", fontstyle='italic',fontsize=10)
plt.xlabel('K values ----->', fontstyle='italic',fontsize=10)
plt.ylabel('Accuracy ---->', fontstyle='italic',fontsize=10)
plt.legend()
plt.show()
clf=KNeighborsClassifier(n_neighbors=18)
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
print(clf.predict([[5.1 ,3.5 ,1.4, 0.2]]))
print(precision_score(y_test,y_pred,average=None))
print(recall_score(y_test,y_pred,average=None))
print(f1_score(y_test,y_pred,average=None))

print(r2_score(y_test,y_pred))

print(classification_report(y_test,y_pred))

print(pd.DataFrame(confusion_matrix(y_test,y_pred),columns=list(range(0,3))))
clf1=KNeighborsClassifier(n_neighbors=30)
clf1.fit(x_train[:,0:2],y_train)

# now we will create a decision boundary

a = np.arange(start=x_train[:, 0].min() - 1, stop=x_train[:, 0].max() + 1, step=0.01)
b = np.arange(start=x_train[:, 1].min() - 1, stop=x_train[:, 1].max() + 1, step=0.01)
xx, yy = np.meshgrid(a, b)
input_array = np.array([xx.ravel(), yy.ravel()]).T
print(input_array.shape)
labels = clf1.predict(input_array)
plt.contourf(xx, yy, labels.reshape(xx.shape), alpha=0.2, cmap=plt.cm.RdYlBu)
markers = {0: 'o', 1: 's', 2: '^'}  
for class_value, marker in markers.items():
    plt.scatter(
        x_train[y_train == class_value, 0],
        x_train[y_train == class_value, 1],
        label=f"Class {class_value}",
        marker=marker,
        edgecolor='k',
        s=30,
    )
plt.title("Decision Boundary with Training Data",fontstyle='italic',fontsize=10)
plt.xlabel("Feature 1",fontstyle='italic',fontsize=10)
plt.ylabel("Feature 2",fontstyle='italic',fontsize=10)
plt.legend()
plt.show()

# training test error and test/validation error 
# effect of value of k on the datasets
# conclusion 
# as the value of (k =1) the overfiting of the model will be done and high variance
# as the value of the k(n) underfitting the model will show high bias
# as the value of k increases the decision boundary shape increases the smoothness also increases

error_train=[]
error_test=[]
# you can also also use confusion matrix also for the case of binary class where you calculate erro via sumof wrong prediction/sumof all matrix
for i in range (1,26):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train,y_train)
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train, y_train)
    y_train_pred = knn.predict(x_train)
    train_error_rate = 1 - accuracy_score(y_train, y_train_pred)
    error_train.append(train_error_rate)
    y_test_pred = knn.predict(x_test)
    test_error_rate = 1 - accuracy_score(y_test, y_test_pred)
    error_test.append(test_error_rate)
    
plt.plot(range(1,26),error_train,label='Training error rate ')
plt.plot(range(1,26),error_test,label='Test/Validation error rate ')
plt.xlabel('K label')
plt.ylabel('Error')
plt.legend()
plt.show()
# weighted knn means you calculate all the distance and their inverse and then
# you combined same color weight and add then more wigthed calss is belongs
# to your point.


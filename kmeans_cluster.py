import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv('vk.csv')
print(df.head())

plt.scatter(df['match_id'],df['batsman_runs'],color='blue',edgecolors='k')
plt.show()

wcss=[]
for i in range (1,20):
    km=KMeans(n_clusters=i)
    km.fit_predict(df)
    wcss.append(km.inertia_)


plt.plot(range(1,20),wcss)
plt.show()


X=df.iloc[:,:].values
km=KMeans(n_clusters=5)
y_means=km.fit_predict(X)

h = .02  # step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predict cluster labels for each point in the grid
grid_points = np.array([xx.ravel(), yy.ravel()]).T
Z = km.predict(grid_points)
Z = Z.reshape(xx.shape)

# Plot the decision boundaries
plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)


plt.scatter(X[y_means==0,0],X[y_means==0,1],edgecolors='k',marker='o',alpha=0.9,label="Cluster 0")
plt.scatter(X[y_means==1,0],X[y_means==1,1],edgecolors='k',marker='s',alpha=0.9,label="Cluster 1")
plt.scatter(X[y_means==2,0],X[y_means==2,1],edgecolors='k',marker='^',alpha=0.9,label="Cluster 2")
plt.scatter(X[y_means==3,0],X[y_means==3,1],edgecolors='k',marker='+',alpha=0.9,label="Cluster 3")
plt.scatter(X[y_means==4,0],X[y_means==4,1],edgecolors='k',marker='D',alpha=0.9,label="Cluster 4")

centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5, marker='x')
plt.legend()
plt.grid()
plt.title('K Means Cluster on the basis of id and score ---->',fontstyle='italic')
plt.xlabel("Match_id--->",fontstyle='italic')
plt.ylabel("Score---->",fontstyle='italic')
plt.show()


from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import pandas as pd
import numpy as py
import plotly.express as px
import matplotlib.pyplot as plt


centroids=[(-5,-5,5),(5,5,-5),(3.5,-2.5,4),(-2.5,2.5,-4)]
cluster_std=[1,1,1,1]
x,y=make_blobs(n_samples=200,n_features=3,centers=centroids,random_state=1,cluster_std=cluster_std)
fig=px.scatter_3d(x=x[:,0],y=x[:,1],z=x[:,2])
fig.show()
wcss=[]
for i in range (1,20):
    km=KMeans(n_clusters=i)
    km.fit_predict(x)
    wcss.append(km.inertia_)
    
plt.plot(range(1,20),wcss)
plt.show()
km=KMeans(n_clusters=4)
y_means=km.fit_predict(x)
df=pd.DataFrame()
df['col1']=x[:,0]
df['col2']=x[:,1]
df['col3']=x[:,2]
df['labels']=y_means

fig=px.scatter_3d(df,x='col1',
                  y='col2',
                  z='col3',
                  color='labels',
                  )
fig.show()


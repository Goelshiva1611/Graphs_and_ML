# Density Based Clustering Algorithm 
# Step-1 identifying alll the core points and border points and also identify the noise points 
# step2 create the clusters of unclustered core points
    # create a new cluster
    #assign nearest points to a cluster on the basis of  epsilon value
#step -3 border points ko assign kardo values of nearest clsutered
#step 4 noise points ko alag cluster dedo 

import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

# Generate sample data
X, _ = make_circles(n_samples=500, factor=0.5, noise=0.03, random_state=12)

# Perform DBSCAN clustering
dbscan = DBSCAN(eps=0.1, min_samples=5)
clusters = dbscan.fit_predict(X)

# Plot the clusters
unique_clusters = np.unique(clusters)

for cluster in unique_clusters:
    if cluster == -1:
        # Plot noise points
        plt.scatter(X[clusters == cluster, 0], X[clusters == cluster, 1], 
                    color='k', marker='x', label='Noise')
    else:
        # Plot core and border points
        plt.scatter(X[clusters == cluster, 0], X[clusters == cluster, 1], 
                    label=f"Cluster {cluster}",edgecolors='k',marker='o')

plt.grid()
plt.title("Density Based Clustering Algorithm")
plt.xlabel("Feature 0")
plt.ylabel("Feature 1")
plt.legend()
plt.show()
# no prediction will be there in this algorithm 
# we have make all clusters again for new prediction
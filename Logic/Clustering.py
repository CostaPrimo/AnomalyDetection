import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


#Method that whitens the data
#Prepares the data for both the Kmenas method, but also the VQ method that requires data to have been whitened first
def whitened(data):
    whitened1 = whiten(data)
    return whitened1


#Method that determines the optimal number of clusters for the K-means algorithm, from a sample of n clusters
def silhuettescore(data):
    range_n_clusters = [3]
    max = 0
    count = 0
    silhouette_avg_max = 0
    data1 = data
    for n_clusters in range_n_clusters:
        clusterer = KMeans(n_clusters=n_clusters, random_state=10)
        cluster_labels = clusterer.fit_predict(data1)
        silhouette_avg = silhouette_score(data1, cluster_labels)
        if count == 0:
            max = n_clusters
            silhouette_avg_max = silhouette_avg
            count = count + 1
        elif silhouette_avg_max < silhouette_avg:
            max = n_clusters
            count = count + 1
            silhouette_avg_max = silhouette_avg
        elif silhouette_avg_max > silhouette_avg:
            count = count+1
    return max


#Method that runs kmeans on the data
#Then based on that result a method vq is called using the results from kmeans and the whitened data
#to determine the distance any point has from its own cluster
def kmeanss(data):
    whitened_data = whitened(data)
    silhuettescores = silhuettescore(data)
    centroids,_ = kmeans(whitened_data, silhuettescores)
    clx = vq(whitened_data, centroids)
    return clx


#Method that returns how many anomalies that are in a stream
def getAnomalies(data):
    clx = kmeanss(data)
    distance = np.array(clx[1])
    count1 = 0
    for x in distance:
        if x > 1:
            count1 = count1+1
    return count1

#These if we ever want to see the result in a scatter plot.
#plt.scatter(whitened[:, 0], whitened[:, 1],alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 1], c='g',alpha=0.5)
#plt.show()

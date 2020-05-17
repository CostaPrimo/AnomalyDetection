import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


def whitened(data):
    whitened1 = whiten(data)
    return whitened1


def silhuettescore(data):
    #range_n_clusters = [9, 10, 11, 12, 13, 14]
    range_n_clusters = [3, 4]
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

def kmeanss(data):
    whitened_data = whitened(data)
    silhuettescores = silhuettescore(data)
    centroids,_ = kmeans(whitened_data, silhuettescores)
    clx = vq(whitened_data, centroids)
    #plt.scatter(whitened_data[:, 0], whitened_data[:, 1],alpha=0.5)
    #plt.scatter(centroids[:, 0], centroids[:, 1], c='g',alpha=0.5)
    #plt.show()
    return clx


def getAnomalies(data):
    clx = kmeanss(data)
    distance = np.array(clx[1])
    anomalies = "false"
    count1 = 0
    for x in distance:
        if x > 1:
            anomalies = "true"
            count1 = count1+1
    return count1

#plt.scatter(whitened[:, 0], whitened[:, 1],alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 1], c='g',alpha=0.5)
#plt.show()

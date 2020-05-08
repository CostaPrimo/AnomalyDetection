#from numpy import array
import numpy as np
from scipy.cluster.vq import vq, kmeans, whiten, kmeans2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

test_readings = np.array([[1534929298000.0, 0.0], [1534929301000.0, 0.0], [1534929302000.0, 0.0], [1534929304000.0, 0.0 ], [1534929305000.0 , 0.0] ,[1534929306000.0, 0.0], [1534929311000.0, 0.0], [1534929312000.0, 0.0], [1534929318000.0, 0.0], [1534929321000.0, 0.0]])
test_readings2 = np.array([[12.3,13.1],[12.2,13.4],[12.5,16.3],[11.4,12.1],[10.1,12.4],[17.1,13.5],[12.7,13.9],[12,13],[11.6,11.3],[7.3,6.3],[11.3,0.1]])
test_readings3 = np.array([[
    1516581901000.0,
    79.0
],
[
    1516581931000.0,
    84.0
],
[
    1516581961000.0,
    79.0
],
[
    1516581991000.0,
    84.0
],
[
    1516582247000.0,
    79.0
],
[
    1516582292000.0,
    84.0
],
[
    1516582307000.0,
    79.0
],
[
    1516582337000.0,
    84.0
],
[
    1516582473000.0,
    79.0
],
[
    1516582503000.0,
    84.0
],
[
    1516582849000.0,
    79.0
],
[
    1516582879000.0,
    84.0
],
[
    1516582954000.0,
    79.0
],
[
    1516582969000.0,
    84.0
],
[
    1516583044000.0,
    79.0
],
[
    1516583090000.0,
    84.0
],
[
    1516583390000.0,
    79.0
],
[
    1516583466000.0,
    84.0
],
[
    1516583526000.0,
    79.0
],
[
    1516583601000.0,
    84.0
],
[
    1516583631000.0,
    79.0
],
[
    1516585602000.0,
    73.0
],
[
    1516600448000.0,
    79.0
],
[
    1516600613000.0,
    84.0
],
[
    1516600734000.0,
    79.0
],
[
    1516602645000.0,
    89.0
],
[
    1516602690000.0,
    84.0
],
[
    1516602705000.0,
    79.0
],
[
    1516602781000.0,
    86.0
],
[
    1516602811000.0,
    79.0
],
[
    1516602841000.0,
    84.0
],
[
    1516603338000.0,
    79.0
],
[
    1516603368000.0,
    84.0
],
[
    1516603398000.0,
    79.0
]])


def whitened(data):
    whitened1 = whiten(data)
    return whitened1


def silhuettescore(data):
    range_n_clusters = [2, 3, 4, 5, 6]
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
    return test_readings3, anomalies, " Amount of anomalies: ", count1


print(getAnomalies(test_readings3))


#plt.scatter(whitened[:, 0], whitened[:, 1],alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 1], c='g',alpha=0.5)
#plt.show()

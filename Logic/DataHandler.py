def setUpClustering(time, reading):
    toCluster = []
    returnDict = reading
    for uuid in returnDict:
        toCluster.append([time, returnDict[uuid]])
    return toCluster

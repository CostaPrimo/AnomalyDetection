from Logic import Clustering
import numpy as np

'''
#This module is responsible for setting up and manipulating data
#This is where the streams are played back
#This is where the data is manipulated before clustering
#This is where the clustering is used
'''


#This method synchronizes all streams and keep the 2D array format needed for clustering
#reading is a dictionary with the form {uuid: value, uuid: value, ...}
#time is the time the value has been read at
#Returns a 2D array with the form [[time, value], [time, value], ...]
def setupStreamsClustering(time, reading):
    toCluster = []
    returnDict = reading
    for uuid in returnDict:
        toCluster.append([time, returnDict[uuid]])
    return toCluster


#This method cluster all streams and returns the anomaly count for a given time period with a set interval
#Readings is a dictionary with the form {uuid: [readings], uuid: [readings], ...}
#Returns a 2D array with the form [[starttime, anomalies], [starttime, anomalies], ...]
def clusterAllStreams(readings):
    time = 0
    offset = 0
    toReturn = []
    while time <= 3600000:
        toCluster = []
        while time <= 60000 + offset:
            toCluster += setupStreamsClustering(time, playbackStreams(readings, time))
            time += 3000
        toReturn.append([time-63000, Clustering.getAnomalies(np.array(toCluster))])
        offset += 60000
    return toReturn


#This method clusters every stream separately ove a given time period with a set interval
#Readings is a dictionary with the form {uuid: [readings], uuid: [readings], ...}
#Returns a dictionary with the form [uuid: [starttime, anomalies], uuid: [starttime, anomalies], ...}
def clusterStreams(readings):
    toReturn = {}
    for uuid in readings:
        time = 0
        offset = 0
        data = []
        while time <= 10800000:
            toCluster = []
            while time <= 900000 + offset:
                toCluster += [[time, playbackStream(readings, uuid, time)]]
                time += 1000
            data.append([time-901000, Clustering.getAnomalies(np.array(toCluster))])
            offset += 900000
        toReturn[uuid] = data
    return toReturn


#This method plays back a single stream returning the value of the stream for a given time offset
#Readings is a dictionary with the form {uuid: [readings], uuid: [readings], ...}
#uuid is the stream that is played back
#offset is the time that has passed since the first reading
#Returns the value for the given offset in time
def playbackStream(readings, uuid, offset):
    templist = readings[uuid]
    time = templist[0][0] + offset
    count = 0
    while time >= templist[count][0]:
        if count + 1 < len(templist):
            if time >= templist[count + 1][0]:
                count += 1
            else:
                break
        else:
            break
    return templist[count][1]


#This method plays back all the streams returning the value of the streams for a given time offset
#Readings is a dictionary with the form {uuid: [readings], uuid: [readings], ...}
#offset is the time that has passed since the first reading
#Returns a dictionary with the form {uuid: value, uuid: value, ...}
def playbackStreams(readings, offset):
    returnDict = {}
    for key in readings:
        templist = readings[key]
        time = templist[0][0]+offset
        count = 0
        while time >= templist[count][0]:
            if count+1 < len(templist):
                if time >= templist[count+1][0]:
                    count += 1
                else:
                    break
            else:
                break
        returnDict[key] = templist[count][1]
    return returnDict

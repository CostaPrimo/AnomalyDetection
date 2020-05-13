from Acquaintance import iLogic, iPersistence
import types
from Logic import DataHandler, Clustering
import numpy as np


class logicFacade(iLogic.iLogic):

    def __init__(self):
        self.persistence = iPersistence.iPersistence
        self.test_text = "Fra logic"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return types.MethodType(self, obj)

    def inject_persistence(self, iPersistence):
        self.persistence = iPersistence

    def getStreamStatus(self, streamtype):
        readings = self.persistence.getStreamReadings(streamtype)
        time = 0
        offset = 0
        while time <= 3600000:
            toCluster = []
            while time <= 60000+offset:
                toCluster += DataHandler.setUpClustering(time, self.persistence.playbackReadings(readings, time))
                time += 3000
            print(Clustering.getAnomalies(np.array(toCluster)))
            offset += 60000
        return "success"

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

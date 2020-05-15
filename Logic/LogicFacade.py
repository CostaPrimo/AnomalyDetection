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
        print(DataHandler.clusterStreams(readings))

    def getStreamMetadata(self, streamID):
        return self.persistence.getStreamMetadata()

    def editStreamType(self, streamID, newtype): raise NotImplementedError

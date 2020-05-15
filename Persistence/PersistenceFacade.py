from Acquaintance import iPersistence
from Persistence import StreamHandler
import types

class persistenceFacade(iPersistence.iPersistence):
    def __init__(self):
        self.stream_handler = StreamHandler.StreamHandler()

    def __get__(self, obj, objtype=None):
           print("__get__")
           if obj is None:
               return self
           return types.MethodType(self, obj)

    def setupBuilding(self):
        self.stream_handler.setup_building()

    def getStreamReadings(self, streamtype):
        self.stream_handler.loadModel()
        return self.stream_handler.getStreamReadings(streamtype)

    def getStreamMetadata(self, streamID):
        self.stream_handler.getMetaData(streamID)

    def editStreamType(self, streamID, newtype): raise NotImplementedError

    def saveData(self, key, value): raise NotImplementedError

    def getData(self, key):
        pass

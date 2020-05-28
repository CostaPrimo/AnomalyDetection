from Acquaintance import iPersistence
from Persistence import StreamHandler
import types

class persistenceFacade(iPersistence.iPersistence):
    def __init__(self):
        self.stream_handler = StreamHandler.StreamHandler()
        self.stream_handler.loadModel()

    def __get__(self, obj, objtype=None):
           print("__get__")
           if obj is None:
               return self
           return types.MethodType(self, obj)

    def getStreamReadings(self, streamtype):
        return self.stream_handler.getStreamReadings(streamtype)

    def getStreamMetadata(self, streamID):
        return self.stream_handler.getMetaData(streamID)

    def editStreamType(self, streamID, currenttype, newtype):
        return self.stream_handler.updateStreamType(streamID, currenttype, newtype)

    def saveData(self, key, value): raise NotImplementedError

    def getData(self, key): raise NotImplementedError

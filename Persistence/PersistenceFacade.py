from Acquaintance import iPersistence
from Persistence import StreamHandler


class persistenceFacade(iPersistence.iPersistence):
    def __init__(self):
        self.stream_handler = StreamHandler.StreamHandler()

    def getStreamReadings(self, streamtype):
        #StreamHandler.purge_streams()
        #self.stream_handler.setup_building()
        self.stream_handler.loadModel()
        return self.stream_handler.getStreamIDs(streamtype)

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

    def saveData(self, key, value): raise NotImplementedError

    def getData(self, key):
        pass


from Acquaintance import iPersistence
from Persistence import StreamHandler


class persistenceFacade(iPersistence.iPersistence):

    def getStreamReadings(self, streamtype):
        StreamHandler.purge_streams()

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

    def saveData(self, key, value): raise NotImplementedError

    def getData(self, key):
        pass


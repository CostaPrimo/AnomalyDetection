from Acquaintance import iPersistence


class persistenceFacade(iPersistence.iPersistence):

    def getStreamReadings(self, streamtype):
        return "NotImplementedYet"

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

    def saveData(self, key, value): raise NotImplementedError

    def getData(self, key):
        pass


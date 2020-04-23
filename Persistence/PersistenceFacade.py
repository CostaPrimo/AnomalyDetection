from Acquaintance import iPersistence


class persistenceFacade(iPersistence.iPersistence):
    def __init__(self):
        self.test_text = "Persitence virker"

    def getStreamReadings(self, streamtype):
        return "NotImplementedYet"

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

    def saveData(self, key, value): raise NotImplementedError

    def getData(self, key):
        pass

    def printTest(self):
        print(self.test_text)

from Acquaintance import iPersistence
import types

class persistenceFacade(iPersistence.iPersistence):
    def __init__(self):
        self.test_text = "Persitence virker"

    def __get__(self, obj, objtype=None):
           print("__get__")
           if obj is None:
               return self
           return types.MethodType(self, obj)

    def getStreamReadings(self, streamtype):
        return streamtype + "NotImplementedYet, from persistence facaden"

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

    def saveData(self, key, value): raise NotImplementedError

    def getData(self, key):
        pass

    def printTest(self):
        print(self.test_text)


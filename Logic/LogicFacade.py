from Acquaintance import iLogic, iPersistence
import types


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
        return self.persistence.getStreamReadings(streamtype)

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

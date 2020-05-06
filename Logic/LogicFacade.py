from Acquaintance import iLogic, iPersistence


class logicFacade(iLogic.iLogic):

    def __init__(self):
        self.persistence = iPersistence.iPersistence

    def inject_persistence(self, iPersistence):
        self.persistence = iPersistence

    def getStreamStatus(self, streamtype):
        self.persistence.getStreamReadings("derp")

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

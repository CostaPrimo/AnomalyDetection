from Acquaintance import iLogic, iPersistence


class logicFacade(iLogic.iLogic):

    def __init__(self):
        self.persistence = iPersistence.iPersistence
        self.test_text = ""

    def inject_persistence(self, iPersistence):
        self.persistence = iPersistence
        self.test_text = "Logic Virker"

    def getStreamStatus(self, streamtype): raise NotImplementedError

    def getStreamMetadata(self, streamID): raise NotImplementedError

    def editStreamType(self, streamID, newtype): raise NotImplementedError

    def printTest(self):
        print(self.test_text)

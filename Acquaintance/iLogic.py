from abc import ABC, abstractmethod


class iLogic(ABC):

    @abstractmethod
    def inject_persistence(self, iPersistence): raise NotImplementedError

    @abstractmethod
    def getStreamStatus(self, streamtype): raise NotImplementedError

    @abstractmethod
    def getStreamMetadata(self, streamID): raise NotImplementedError

    @abstractmethod
    def editStreamType(self, streamID, newtype): raise NotImplementedError

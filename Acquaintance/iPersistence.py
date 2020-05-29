from abc import ABC, abstractmethod


class iPersistence(ABC):

    @abstractmethod
    def getStreamReadings(self, streamtype): raise NotImplementedError

    @abstractmethod
    def getStreamMetadata(self, streamID): raise NotImplementedError

    @abstractmethod
    def editStreamType(self, streamID, currenttype, newtype): raise NotImplementedError


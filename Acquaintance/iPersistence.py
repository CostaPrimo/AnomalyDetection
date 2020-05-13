from abc import ABC, abstractmethod


class iPersistence(ABC):

    @abstractmethod
    def getStreamReadings(self, streamtype): raise NotImplementedError

    @abstractmethod
    def getStreamMetadata(self, streamID): raise NotImplementedError

    @abstractmethod
    def editStreamType(self, streamID, newtype): raise NotImplementedError

    @abstractmethod
    def saveData(self, key, value): raise NotImplementedError

    @abstractmethod
    def getData(self, key): raise NotImplementedError

    @abstractmethod
    def playbackReadings(self, readings, offset): raise NotImplementedError

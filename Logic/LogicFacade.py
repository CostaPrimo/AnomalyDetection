from Acquaintance import iLogic, iPersistence
import types
from Logic import DataHandler


class logicFacade(iLogic.iLogic):

    def __init__(self):
        self.persistence = iPersistence.iPersistence
        self.humidityreadings = {}
        self.temperaturereadings = {}
        self.co2readings = {}

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return types.MethodType(self, obj)

    def inject_persistence(self, iPersistence):
        self.persistence = iPersistence
        print("Loading readings")
        self.humidityreadings = self.persistence.getStreamReadings("humidity")
        self.temperaturereadings = self.persistence.getStreamReadings("temperature")
        self.co2readings = self.persistence.getStreamReadings("co2")
        print("Readings loaded")

    def getStreamStatus(self, streamtype):
        if streamtype == "humidity":
            return DataHandler.clusterStreams(self.humidityreadings)
        elif streamtype == "temperature":
            return DataHandler.clusterStreams(self.temperaturereadings)
        elif streamtype == "co2":
            return DataHandler.clusterStreams(self.co2readings)
        else:
            return "No such type"

    def getStreamMetadata(self, streamID):
        return self.persistence.getStreamMetadata(streamID)

    #NotSupported
    #NotTested
    def editStreamType(self, streamID, newtype):
        return self.persistence.editStreamType(streamID, newtype)

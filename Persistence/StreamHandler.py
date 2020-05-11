from rdflib import Graph, Namespace, URIRef, Literal
import rdflib
import json
import os
import requests


RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
BRICK = Namespace('https://brickschema.org/schema/1.1.0/Brick#')
N = Namespace('http://bachelor.sdu.dk/jeppe_nick/test/example#')


'''
#Method used to remove streams without readings, list stream types, and count each type of stream
def count_and_purge_streams():
    stream_descriptions = []
    stream_counts = {}
    for file in os.listdir("Persistence/streams"):
        tempfile = (os.path.join("Persistence/streams", file))
        with open(tempfile) as json_file:
            data = json.load(json_file)
            if 'Readings' in data and len(data['Readings']) != 0:
                if metadata['Description'] in stream_descriptions:
                    count = stream_counts[metadata['Description']]
                    stream_counts[metadata['Description']] = count+1
                else:
                    stream_descriptions.append(metadata['Description'])
                    stream_counts[metadata['Description']] = 1
            else:
                os.remove(tempfile)
                print("file deleted")
            metadata = data['Metadata']
    print(stream_counts)
'''


class StreamHandler:
    def __init__(self):
        self.g = Graph()
        self.files = []

#For creating brick model of our fictive building
#----------------------------------------------------------------------------------------------------------------------

    #Setup the foundation for the Brick modelling of the build
    #Determines which sensor types will be added to the model of the building
    def model(self):
        del self.g
        self.g = Graph()
        brickpath = lambda filename: 'Persistence/' + filename
        self.g.parse(brickpath('Brick_expanded.ttl'), format='turtle')

        self.g.bind('rdf', RDF)
        self.g.bind('rdfs', RDFS)
        self.g.bind('owl', OWL)
        self.g.bind('brick', BRICK)
        self.g.bind('n', N)
        for file in os.listdir("Persistence/streams"):
            tempfile = (os.path.join("Persistence/streams", file))
            with open(tempfile) as json_file:
                data = json.load(json_file)
                metadata = data['Metadata']
                description = metadata['Description']
                if description == "Temperature Value" or description == 'CO2 Value' or description == 'Humidity':
                    self.files.append(tempfile)

    #Setup the building model and saves it
    #1 Building, 1 Floor, 1 Room for every sensor
    def setup_building(self):
        del self.g
        self.g = Graph()
        self.model()
        building = N['/building']
        self.g.add((building, RDF.type, BRICK['Building']))
        floor = N['/building/floors/0']
        self.g.add((floor, RDF.type, BRICK['Floor']))
        self.g.add((building, BRICK.contains, floor))
        rooms = []
        roomnames = []
        for number in range(len(self.files)):
            room = N['building/rooms/room_%s' % number]
            self.g.add((room, RDF.type, BRICK['Room']))
            self.g.add((room, BRICK.label, Literal('room %s' % number)))
            self.g.add((floor, BRICK.contains, room))
            rooms.append(room)
            roomnames.append("room_%s" % number)
        for file in self.files:
            UUID = ""
            metadata = ""
            description = ""
            with open(file) as json_file:
                data = json.load(json_file)
                metadata = data['Metadata']
                UUID = data['uuid']
                description = metadata['Description']
            if description == 'Temperature Value':
                sensor = N['building/rooms/%s/temp-sensor' % roomnames.pop(0)]
                self.g.add((sensor, RDF.type, BRICK['Temperature_Sensor']))
                self.g.add((sensor, BRICK.label, Literal(UUID)))
                self.g.add((sensor, BRICK.pointOf, rooms.pop(0)))
            elif description == 'CO2 Value':
                sensor = N['building/rooms/%s/co2-sensor' % roomnames.pop(0)]
                self.g.add((sensor, RDF.type, BRICK['CO2_Sensor']))
                self.g.add((sensor, BRICK.label, Literal(UUID)))
                self.g.add((sensor, BRICK.pointOf, rooms.pop(0)))
            elif description == 'Humidity':
                sensor = N['building/rooms/%s/humidity' % roomnames.pop(0)]
                self.g.add((sensor, RDF.type, BRICK['Humidity']))
                self.g.add((sensor, BRICK.label, Literal(UUID)))
                self.g.add((sensor, BRICK.pointOf, rooms.pop(0)))
        self.g.serialize('Persistence/building_test3.ttl', 'turtle')

#For loading our model and accessing/altering information in it
#----------------------------------------------------------------------------------------------------------------------

    #Loads the building model
    def loadModel(self):
        del self.g
        self.g = Graph()
        self.g.parse('Persistence/building_test3.ttl', format='turtle')

    #Queries on the model
    def query(self, q):
        r = self.g.query(q)
        return list(map(lambda row: list(row), r))

    #Alters information in the model
    def update(self, q):
        r = self.g.update(q)

    #Cleans up the information from the query and return it in a json structure
    def pprint(self, structure):
        pretty = json.dumps(structure, sort_keys=True, indent=4, separators=(',', ': '))
        return pretty

#Methods for extracting and manipulating data
# ----------------------------------------------------------------------------------------------------------------------

    #Given a type match, return IDs for all the streams of that type
    #Returns an array with the following structure [[UUID],[UUID],...]
    def getStreamIDs(self, type):
        if type == 'temperature':
            stream_q = \
            '''
            SELECT DISTINCT ?sensor_uuid
                WHERE {
                    ?room     rdf:type/brick:subClassOf* brick:Room .
                    ?sensor   rdf:type/brick:subClassOf* brick:Temperature_Sensor .
                    
                    ?sensor   brick:pointOf ?room .

                    ?sensor   brick:label ?sensor_uuid .
                }
            '''
            return self.pprint(self.query(stream_q))
        elif type == 'co2':
            stream_q = \
                '''
                SELECT DISTINCT ?sensor_uuid
                WHERE {
                    ?room     rdf:type/brick:subClassOf* brick:Room .
                    ?sensor   rdf:type/brick:subClassOf* brick:CO2_Sensor .
                    
                    ?sensor   brick:pointOf ?room .

                    ?sensor   brick:label ?sensor_uuid .
                }
                '''
            return self.pprint(self.query(stream_q))
        elif type == 'humidity':
            stream_q = \
                '''
                SELECT DISTINCT ?sensor_uuid
                WHERE {
                    ?room     rdf:type/brick:subClassOf* brick:Room .
                    ?sensor   rdf:type/brick:subClassOf* brick:Humidity .
                    
                    ?sensor   brick:pointOf ?room .

                    ?sensor   brick:label ?sensor_uuid .
                }
                '''
            return self.pprint(self.query(stream_q))
        else:
            return "No such type"

    #Given a list of streamsIDs find their respective readings and return them
    #Returns a Dictionary with the form {UUID: [Readings], UUID: [Readings,...}
    def findFileReadings(self, streams):
        rstreams = {}
        if streams == "No such type":
            return rstreams
        else:
            ids = streams.replace(' ', '').replace('[', '').replace(']', '').replace('\n', '').replace('"', '').split(
                ',')
            for uuid in ids:
                with open("Persistence/streams/%s.json" % uuid)as json_file:
                    data = json.load(json_file)
                    rstreams[uuid] = data['Readings']
            return rstreams

    #Given a Dictionary wih UUIDs and readings, return the reading after 0 ms offset
    #Returns a Dictionary with the form {UUID: Reading, UUID: Reading, ...}
    def playbackStreams(self, readings, offset):
        returnDict = {}
        for key in readings:
            templist = readings[key]
            time = templist[0][0]+offset
            count = 0
            while time >= templist[count][0]:
                if count+1 < len(templist):
                    if time >= templist[count+1][0]:
                        count += 1
            returnDict[key] = templist[count][1]
        return returnDict

#Method to be called in the facade
#---------------------------------------------------------------------------------------------------------------------
    def getStreamReadings(self, type):
        readings = self.findFileReadings(self.getStreamIDs(type))
        return self.playbackStreams(readings, 3600000)
#---------------------------------------------------------------------------------------------------------------------

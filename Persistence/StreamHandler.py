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


def purge_streams():
    stream_descriptions = []
    stream_counts = {}
    for file in os.listdir("Persistence/streams"):
        tempfile = (os.path.join("Persistence/streams", file))
        with open(tempfile) as json_file:
            data = json.load(json_file)
            metadata = data['Metadata']
            if metadata['Description'] in stream_descriptions:
                count = stream_counts[metadata['Description']]
                stream_counts[metadata['Description']] = count+1
            else:
                stream_descriptions.append(metadata['Description'])
                stream_counts[metadata['Description']] = 1
    print(stream_counts)
    '''
        if 'Readings' in data and len(data['Readings']) != 0:
            print(data['Metadata'])
        else:
            os.remove(tempfile)
            print("file deleted")
    '''


class StreamHandler:
    def __init__(self):
        self.g = Graph()
        self.files = []
        for file in os.listdir("Persistence/streams"):
            tempfile = (os.path.join("Persistence/streams", file))
            with open(tempfile) as json_file:
                data = json.load(json_file)
                metadata = data['Metadata']
                description = metadata['Description']
                if description == "Temperature Value" or description == 'CO2 Value' or description == 'Humidity':
                    self.files.append(tempfile)

    def setup_building(self):
        del self.g
        self.g = Graph()
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
        self.g.serialize('Persistence/building_test.ttl', 'turtle')

    def model(self):
        brickpath = lambda filename: 'Persistence/' + filename
        self.g.parse(brickpath('Persistence/Brick_expanded.ttl'), format='turtle')

        self.g.bind('rdf', RDF)
        self.g.bind('rdfs', RDFS)
        self.g.bind('owl', OWL)
        self.g.bind('brick', BRICK)
        self.g.bind('n', N)

    def loadModel(self):
        del self.g
        self.g = Graph()
        self.g.parse('Persistence/building_test.ttl', format='turtle')

    def getStreamIDs(self, type):
        stream_q = ""
        if type == 'temperature':
            stream_q = \
            '''
            SELECT DISTINCT ?sensor_uuid
            WHERE {
                ?sensor   rdf:type/brick:subClassOf* brick:Temperature_Sensor .
                
                ?sensor   brick:label ?sensor_uuid .
            }
            '''
            self.pprint(self.query(stream_q))
            return "success"
        elif type == 'co2':
            stream_q = \
                '''
                SELECT DISTINCT ?sensor_uuid
                WHERE {
                    ?sensor   rdf:type/brick:subClassOf* brick:CO2_Sensor .

                    ?sensor   brick:label ?sensor_uuid .
                }
                '''
            self.pprint(self.query(stream_q))
            return "success"
        elif type == 'humidity':
            stream_q = \
                '''
                SELECT DISTINCT ?sensor_uuid
                WHERE {
                    ?sensor   rdf:type/brick:subClassOf* brick:Humidity .

                    ?sensor   brick:label ?sensor_uuid .
                }
                '''
            self.pprint(self.query(stream_q))
            return "success"
        else:
            return "No such type"

#---------------------------------------------------------------------------------------------------------------------

    def query(self, q):
        r = self.g.query(q)
        return list(map(lambda row: list(row), r))

    def update(self, q):
        r = self.g.update(q)

    def pprint(self, structure):
        pretty = json.dumps(structure, sort_keys=True, indent=4, separators=(',', ': '))
        print(pretty)


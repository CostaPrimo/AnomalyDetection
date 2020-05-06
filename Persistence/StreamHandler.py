from rdflib import Graph, Namespace, URIRef, Literal
import rdflib
import json
import os

RDF = Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
OWL = Namespace('http://www.w3.org/2002/07/owl#')
BRICK = Namespace('https://brickschema.org/schema/1.1.0/Brick#')
N = Namespace('')##SPØRG TIL DET HER (Hvad skal det bruges til)


def purge_streams():
    stream_descriptions = []
    stream_counts = {}
    for file in os.listdir("Persistence/streams"):
        tempfile = (os.path.join("Persistence/streams", file))
        data = ""
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
        self.brickpath = lambda filename: '../Persistence/streams/' + filename #SPØRG TIL DET HER (Hvordan skal path se ud?)
        self.g.parse(self.brickpath('../Persistence/Brick_expanded.ttl'), format='turtle') #SPØRG TIL DET HER (Skal denne path være den sammme?)
        self.g.bind('rdf', RDF)
        self.g.bind('rdfs', RDFS)
        self.g.bind('owl', OWL)
        self.g.bind('brick', BRICK)
        self.g.bind('n', N)
        self.files = []
        for file in os.listdir("/streams"):
            tempfile = (os.path.join("/streams", file))
            with open(file) as json_file:
                data = json.load(json_file)
                if "Readings" in data:
                    self.files.append(tempfile)
                    print(tempfile)


    def setupBuilding(self):
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
            Description = ""
            Modality = ""
            with open(file) as json_file:
                data = json.load(json_file)
                UUID = data['uuid']
                Description = data['Description']
                Modality = data['Modality']
            sensor = N['building/rooms/%s/sensor' % roomnames.pop(0)]
            self.g.add((sensor, RDF.type, BRICK['Sensor']))
            self.g.add((sensor, BRICK.label, Literal(UUID)))
            self.g.add((sensor, BRICK.pointOf, rooms.pop(0)))
        self.g.serialize('../Persistence/building.ttl', 'turtle')
        del self.g
        self.g = Graph()
        self.g.parse('../Persistence/building.ttl', format='turtle')


    '''
    def model(self):
        g = Graph()

        brickpath = lambda filename: '../Persistence/Streams/' + filename ##SPØRG TIL DET HER (Hvordan skal path se ud?)
        g.parse(brickpath('../Persistence/Brick_expanded.ttl'), format='turtle') ##SPØRG TIL DET HER (Skal denne path være den sammme?)

        g.bind('rdf', RDF)
        g.bind('rdfs', RDFS)
        g.bind('owl', OWL)
        g.bind('brick', BRICK)
        g.bind('n', N)

        return g
    '''

    def query(g, q):
        r = g.query(q)
        return list(map(lambda row: list(row), r))


    def update(g, q):
        r = g.update(q)


'''
    def pprint(structure):
        pretty = json.dumps(structure, sort_keys=True, indent=4, separators=(',', ': '))
        print(pretty)
'''

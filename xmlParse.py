import xmltodict
import xml.etree.ElementTree as ET

actionsFile = '../../Resources/actions.xml'
settingsFile = '../../Resources/settings.xml'

neighboursForGivenNode = []
personalities = []
nodes = []
edges = []


def getPersonalityNames():
    settingsDoc = getDocForXmlFile(settingsFile)
    for personality in settingsDoc["settings"]["personalitynames"]["personality"]:
        dict = {}
        dictData = {}
        dictData["name"] = personality["name"].encode('ascii')
        dictData["id"] = personality["id"].encode('ascii')
        dict["data"] = dictData
        personalities.append(dict)

    return personalities


def parse():
    global edges
    modifiers = []
    doc = getDocForXmlFile(actionsFile)

    for action in toList(doc["actions"]["action"]):
        dict = {}
        dictData = {}

        dictData["id"] = action["actionId"].encode('ascii')
        dictData["name"] = action["actionname"].encode('ascii')
        dictData["animationname"] = action["animationname"].encode('ascii')
        dictData["modifiers"] = []

        if action["modifiers"] != None:
            for modifier in toList(action["modifiers"]["modifier"]):
                dictModifier = {}
                dictModifier["id"] = modifier["id"].encode('ascii')
                dictModifier["value"] = modifier["value"].encode('ascii')
                dictData["modifiers"].append(dictModifier)

        dictPosition = {}
        dictPosition["x"] = action["position"]["x"].encode('ascii')
        dictPosition["y"] = action["position"]["y"].encode('ascii')
        dictPosition["z"] = action["position"]["z"].encode('ascii')

        dictData["position"] = dictPosition

        dict["data"] = dictData
        nodes.append(dict)
        edges = edges + getNeighboursAsEdge(action)

    return nodes, edges


def getNeighboursAsEdge(action):
    neighbourEdges = []
    if bool(action["neighbours"]):
        for neighbour in toList(action["neighbours"]["neighbour"]):
            edge = {}
            edgeData = {}
            edgeData["id"] = neighbour + "." + action["actionId"].encode('ascii')
            edgeData["source"] = action["actionId"].encode('ascii')
            edgeData["target"] = neighbour
            for node in nodes:
                if node["data"]["id"] == neighbour:
                    edgeData["name"] = node["data"]["name"].encode('ascii')
            edge["data"] = edgeData
            neighbourEdges.append(edge)

    return neighbourEdges


def saveGraph(graph):
    tree = ET.ElementTree(ET.fromstring(graph))
    tree.write(actionsFile)


def getDocForXmlFile(fileName):
    with open(fileName) as fd:
        return xmltodict.parse(fd.read())

def toList(object):
    return object if type(object) is list else [object]
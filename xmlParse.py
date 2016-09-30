import xmltodict
import xml.etree.ElementTree as ET

actionsFile = 'resources/actions.xml'
settingsFile = 'resources/settings.xml'

neighboursForGivenNode = []
personalities = []
nodes = []
edges = []


def getPersonalityNames():
    settingsDoc = getDocForXmlFile(settingsFile)
    for personality in settingsDoc["settings"]["personalities"]["personality"]:
        dict = {}
        dictData = {}
        dictData["name"] = personality["name"]
        dictData["id"] = personality["id"]
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

        dictData["id"] = action["actionId"]
        dictData["name"] = action["actionname"]
        dictData["animationname"] = action["animationname"]
        dictData["modifiers"] = []

        if action["modifiers"] != None:
            for modifier in toList(action["modifiers"]["modifier"]):
                dictModifier = {}
                dictModifier["id"] = modifier["id"]
                dictModifier["value"] = modifier["value"]
                dictData["modifiers"].append(dictModifier)

        dictPosition = {}
        dictPosition["x"] = action["position"]["x"]
        dictPosition["y"] = action["position"]["y"]
        dictPosition["z"] = action["position"]["z"]

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
            edgeData["id"] = neighbour + "." + action["actionId"]
            edgeData["source"] = action["actionId"]
            edgeData["target"] = neighbour
            for node in nodes:
                if node["data"]["id"] == neighbour:
                    edgeData["name"] = node["data"]["name"]
            edge["data"] = edgeData
            neighbourEdges.append(edge)

    return neighbourEdges


def saveGraph(graph):
    tree = ET.ElementTree(ET.fromstring(graph))
    tree.write('resources/actions.xml')


def getDocForXmlFile(fileName):
    with open(fileName) as fd:
        return xmltodict.parse(fd.read())

def toList(object):
    return object if type(object) is list else [object]
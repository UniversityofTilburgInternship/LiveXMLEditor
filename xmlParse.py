import xmltodict
import xml.etree.ElementTree as ET

actionsFile = 'resources/actions.xml'
settingsFile = 'resources/settings.xml'

neighboursForGivenNode = []
personalities = []
nodes = []
edges = []


def getNeighboursForGivenNode(nodeId):
    doc = getDocForXmlFile(actionsFile)
    neighboursForGivenNode = []

    for action in doc["actions"]["action"]:
        if (int(action["actionId"]) == nodeId):
            neighboursForGivenNode = getNeighboursData(action)

    return neighboursForGivenNode


def getPersonalityNames():
    settingsDoc = getDocForXmlFile(settingsFile)
    for personality in settingsDoc["settings"]["personalities"]["personality"]:
        dict = {}
        dictData = {}
        dictData["name"] = personality["name"]
        dict["data"] = dictData
        personalities.append(dict)

    return personalities


def parse():
    global edges
    modifiers = []
    doc = getDocForXmlFile(actionsFile)

    for action in doc["actions"]["action"]:
        dict = {}
        dictData = {}

        dictData["id"] = action["actionId"]
        dictData["name"] = action["actionname"]
        dictData["animationname"] = action["animationname"]
        dictData["modifiers"] = []

        for modifier in action["modifiers"]["modifier"]:
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
        for neighbour in action["neighbours"]["neighbour"]:
            edge = {}
            edgeData = {}
            edgeData["id"] = neighbour + "." + action["actionId"]
            edgeData["source"] = action["actionId"]
            edgeData["target"] = neighbour
            edge["data"] = edgeData
            neighbourEdges.append(edge)

    return neighbourEdges


def getNeighboursData(action):
    if bool(action['neighbours']["neighbour"]):
        neighbourData = {}
        for neighbour in action['neighbours']["neighbour"]:
            neighbourToBeInserted = {}
            currentNeighbour = {}
            currentNeighbour["id"] = neighbour["id"]
            neighbourToBeInserted["data"] = currentNeighbour
            neighbourData.append(neighbourToBeInserted)

def removeNeighbourFromXml(neighourId, rootNode):
    tree = ElementTree()
    tree.parse('resources/actions.xml')
    actions = tree.findall('action')
    for action in actions:
        if(int(action.find('actionId').text) == rootNode):
            neighbours = action.find('neighbours')
            for neighbour in neighbours:
                if(int(neighbour.text) == neighourId):
                    print('Removing ' + str(neighbour))
                    neighbours.remove(neighbour)

    #disabled for debugging
    tree.write('resources/actions.xml')


def saveGraph(graph):
    tree = ET.ElementTree(ET.fromstring(graph))
    tree.write('resources/actions.xml')


def getDocForXmlFile(fileName):
    with open(fileName) as fd:
        return xmltodict.parse(fd.read())

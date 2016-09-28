import xmltodict
from xml.etree.ElementTree import ElementTree, Element

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
    doc = getDocForXmlFile(actionsFile)

    for action in doc["actions"]["action"]:
        dict = {}
        dictData = {}
        dictData["id"] = action["actionId"]
        dictData["name"] = action["actionname"]
        dictData["animationname"] = action["animationname"]
        dict["data"] = dictData
        nodes.append(dict)
        edges = edges + getNeighboursAsEdge(action)

    return nodes, edges


def getNeighboursAsEdge(action):
    if bool(action["neighbours"]["neighbour"]):
        neighbourEdges = []
        for neighbour in action["neighbours"]["neighbour"]:
            print('Action id ' + action["actionId"] + ' has neighbour ' + neighbour)
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

def addEdgeToXml(neighourId, rootNode):
    tree = ElementTree()
    tree.parse('resources/actions.xml')

    actions = tree.findall('action')
    for action in actions:
        if(int(action.find('actionId').text) == rootNode):
            neighbours = action.find('neighbours')
            neighbour = Element('neighbour')
            neighbour.text = str(neighourId)
            neighbours.append(neighbour)

            #disabled for debugging
            tree.write('resources/actions.xml')

def removeNodeFromXml(id):
    tree = ElementTree()
    tree.parse('resources/actions.xml')
    actions = tree.getroot()
    for action in actions:
        removeNeighbourFromXml(int(id), int(action.find('actionId').text))
        if(int(action.find('actionId').text) == id):
            actions.remove(action)
    tree.write('resources/actions.xml')






def getDocForXmlFile(fileName):
    with open(fileName) as fd:
        return xmltodict.parse(fd.read())

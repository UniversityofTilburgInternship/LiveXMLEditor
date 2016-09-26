import xmltodict

neighboursForGivenNode = []
personalities = []
nodes = []
edges = []

def getNeighboursForGivenNode(nodeId):
    with open('resources/actions.xml') as fd:
        doc = xmltodict.parse(fd.read())
        neighboursForGivenNode = []

        for action in doc["actions"]["action"]:
            if(int(action["actionId"]) == nodeId):
                neighboursForGivenNode = getNeighboursData(action)

        return neighboursForGivenNode

def getPersonalityNames():
    with open('resources/settings.xml') as settingsFile:
        settingsDoc = xmltodict.parse(settingsFile.read())

        for personality in settingsDoc["settings"]["personalities"]["personality"]:
            dict = {}
            dictData ={}
            dictData["name"] = personality["name"]
            dict["data"] = dictData
            personalities.append(dict)

    return personalities

def parse():
    global edges
    with open('resources/actions.xml') as fd:
        doc = xmltodict.parse(fd.read())

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
            edgeData["source"] = action["actionId"]
            edgeData["target"] = neighbour
            edge["data"] = edgeData
            neighbourEdges.append(edge)

    return neighbourEdges

def getNeighbourData(action):
    if bool(action['neighbours']["neighbour"]):
        neighbourData = {}
        for neighbour in action['neighbours']["neighbour"]:
            neighbourToBeInserted = {}
            currentNeighbour = {}
            currentNeighbour["id"] = neighbour["id"]
            neighbourToBeInserted["data"] = currentNeighbour
            neighbourData.append(neighbourToBeInserted)


import xmltodict

nodes = []
edges = []

def parse():
    with open('resources/actions.xml') as fd:
        doc = xmltodict.parse(fd.read())

        for action in doc["actions"]["action"]:
            dict = {}
            dictData = {}
            dictData["id"] = action["actionId"]
            dictData["name"] = action["actionname"]
            dict["data"] = dictData
            nodes.append(dict)

            if bool(action['neighbours']["neighbour"]):
                for neighbour in action['neighbours']["neighbour"]:
                    edge = {}
                    edgeData = {}
                    edgeData["source"] = dictData["id"]
                    edgeData["target"] = neighbour
                    edge["data"] = edgeData
                    edges.append(edge)

    return nodes, edges
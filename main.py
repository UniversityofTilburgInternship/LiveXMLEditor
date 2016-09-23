import json

import xmltodict
from bottle import route, run, template, static_file, request

nodes = []
edges = []

counter = 500
def parse():
    global  counter
    with open('resources/actions.xml') as fd:
        doc = xmltodict.parse(fd.read())

        for action in doc["actions"]["action"]:
            dict = {}
            dictData = {}
            dictPosition = {}
            dictData["id"] = action["actionId"]
            dictData["idInt"] = int(action["actionId"])
            dictData["name"] = action["actionname"]
            dictPosition["x"] = 5
            dictPosition["y"] = 5
            dict["data"] = dictData
            dict["position"] = dictPosition
            nodes.append(dict)

            if bool(action['neighbours']["neighbour"]):
                for neighbour in action['neighbours']["neighbour"]:
                    edge = {}
                    edgeData = {}
                    edgeData["id"] = str(counter)
                    edgeData["source"] = dictData["id"]
                    edgeData["target"] = neighbour
                    edgeData["weight"] = 0.5
                    edge["data"] = edgeData
                    nodes.append(edge)
                    counter += 1


parse()


@route('/')
def index():
    global nodes
    return template('index', res=json.dumps(nodes))

@route('/', method='POST')
def index():
    postdata = request.body.read()
    print(postdata)


run(host='localhost', port=8080)

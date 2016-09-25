import json
<<<<<<< HEAD
import webbrowser

import tkinter as tk
from tkinter import filedialog
from bottle import route, run, template, static_file, request
from xmlParse import parse

# Commented for debug purposes - DO NOT DELTE!
# root = tk.Tk()
# root.withdraw()
# file = filedialog.askopenfilename()

=======

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
>>>>>>> 4d11f28654b61aa40f784a13edda03835cf098d0

nodes, edges = parse()


@route('/')
def index():
    global nodes
<<<<<<< HEAD
    return template('index', nodes=json.dumps(nodes), edges=json.dumps(edges))
=======
    return template('index', res=json.dumps(nodes))
>>>>>>> 4d11f28654b61aa40f784a13edda03835cf098d0

@route('/', method='POST')
def index():
    postdata = request.body.read()
    print(postdata)
<<<<<<< HEAD
=======

>>>>>>> 4d11f28654b61aa40f784a13edda03835cf098d0

webbrowser.open('http://localhost:8080')
run(host='localhost', port=8080)

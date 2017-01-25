import json
import webbrowser
import dicttoxml
import tkinter as tk
from tkinter import filedialog
from bottle import route, run, template, static_file, request
from xmlParse import saveGraph, parse, getPersonalityNames

# Commented for debug purposes - DO NOT DELTE!
# root = tk.Tk()
# root.withdraw()
# fileSettings = filedialog.askopenfilename()

personalities = getPersonalityNames()
nodes, edges = parse()
print personalities

@route('/')
def index():
    global nodes
    return template('index', actions=nodes, nodes=json.dumps(nodes), edges=json.dumps(edges),
                    personalities=personalities)


@route('/', method='POST')
def index():
    graph = request.params.get('graph', 0)
    saveGraph(graph)

@route('/', method='PUT')
def index():
    neighbourNodeId = request.params.get('neighbourId', 0, type=int)
    rootNodeId = request.params.get('rootId', 0, type=int)
    addEdgeToXml(neighbourNodeId, rootNodeId)


@route('/', method='DELETE')
def index():
    nodeId = request.params.get('node', 0, type=int)
    removeNodeFromXml(nodeId)


webbrowser.open('http://localhost:8080')
run(host='localhost', port=8080)

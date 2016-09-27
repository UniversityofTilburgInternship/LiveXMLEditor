import json
import webbrowser

import tkinter as tk
from tkinter import filedialog
from bottle import route, run, template, static_file, request
from xmlParse import parse, getPersonalityNames, removeNeighbourFromXml

# Commented for debug purposes - DO NOT DELTE!
# root = tk.Tk()
# root.withdraw()
# file = filedialog.askopenfilename()

personalities = getPersonalityNames()
nodes, edges = parse()

@route('/')
def index():
    global nodes
    return template('index',actions=nodes, nodes=json.dumps(nodes), edges=json.dumps(edges), personalities=personalities)

@route('/', method='POST')
def index():
    neighbourNodeId = request.params.get('neighbourId', 0, type=int)
    rootNodeId = request.params.get('rootId', 0, type=int)
    removeNeighbourFromXml(neighbourNodeId, rootNodeId)


webbrowser.open('http://localhost:8080')
run(host='localhost', port=8080)
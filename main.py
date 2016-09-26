import json
import webbrowser

import tkinter as tk
from tkinter import filedialog
from bottle import route, run, template, static_file, request
from xmlParse import parse, getPersonalityNames, getNeighboursForGivenNode

# Commented for debug purposes - DO NOT DELTE!
# root = tk.Tk()
# root.withdraw()
# file = filedialog.askopenfilename()

personalities = getPersonalityNames()
nodes, edges = parse()

for edge in edges:
    print(edge)


@route('/')
def index():
    global nodes
    return template('index', nodes=json.dumps(nodes), edges=json.dumps(edges), personalities=personalities)

@route('/', method='POST')
def index():
    nodeId = request.body.read()
    print(getNeighboursForGivenNode(nodeId))

webbrowser.open('http://localhost:8080')
run(host='localhost', port=8080)

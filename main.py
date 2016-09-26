import json
import webbrowser

import tkinter as tk
from tkinter import filedialog
from bottle import route, run, template, static_file, request
from xmlParse import parse

# Commented for debug purposes - DO NOT DELTE!
# root = tk.Tk()
# root.withdraw()
# file = filedialog.askopenfilename()




nodes, edges = parse()


@route('/')
def index():
    global nodes
    return template('index', nodes=json.dumps(nodes), edges=json.dumps(edges))

@route('/', method='POST')
def index():
    postdata = request.body.read()
    print(postdata)

webbrowser.open('http://localhost:8080')
run(host='localhost', port=8080)

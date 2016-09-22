import xmltodict
from bottle import route, run, template, static_file

list = []

def parse():
    global  list
    with open('resources/actions.xml') as fd:
        doc = xmltodict.parse(fd.read())

        for action in doc["actions"]["action"][0]:
            print(action)
            list.append(action)


parse()

@route('/')
def index():
    global  list
    return template('index', res=list)

run(host='localhost', port=8080)

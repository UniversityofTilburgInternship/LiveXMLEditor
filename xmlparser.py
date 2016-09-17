from http.server import BaseHTTPRequestHandler, HTTPServer
import xml.etree.ElementTree
from htmlWriter import htmlWriter


class xmlParser():

  def __init__(self,fileToParse):
      self.FileToParse = fileToParse

  def getXmlValuesTable(self):
      e = xml.etree.ElementTree.parse(self.FileToParse).getroot()
      tableMid = """
                    <h1>Action.xml content</h1>
                    <table class='table'>
                        <th>Action ID</th>
                        <th>Action Name</th>
                        <th>Animation</th>
                 """
      for anAction in e.findall('action'):
         tableMid+= '<tr>'
         for actionAttribute in anAction:
            if(actionAttribute.tag == 'actionId' or actionAttribute.tag == 'actionname'
		    or actionAttribute.tag == 'animationname'):
               tableMid += '<td>' + actionAttribute.text + '</td>'
         tableMid += '</tr>'
 
      tableMid += "</table>"
      return tableMid

  def getFullHtml(self):
      htmlwriter = htmlWriter()
      return htmlwriter.getHeadHtml() + self.getXmlValuesTable() + htmlwriter.getTailHtml()

    


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  def do_POST(self):
        """Handle a post request by returning the square of the number."""
        length = int(self.headers['content-length'])        
        data_string = self.rfile.read(length)

        data_string = data_string.decode("utf-8")

        self.wfile.write(bytes(data_string, "utf8"))

        #change xml file accordingly



  #Handle get request by sending self a 200 status code and printing the HTML.
  def do_GET(self): 
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client TODO: Define the html in a class or so.
        parser = xmlParser('actions.xml')
        message = parser.getFullHtml()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

#end of class
 
def run():
  print('Starting python server...')
 
  # Server settings
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('Running python server!')
  httpd.serve_forever()

 
run()

import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('actions.xml').getroot()

tableBegin = "<table><tr>Action Id</tr><tr>Action Name</tr><tr>Action Animation</tr>"
tableMid = ""
tableEnd = "</table>"

for anAction in e.findall('action'):
	for actionAttribute in anAction:
		if(actionAttribute.tag == 'actionId' 
		   or actionAttribute.tag == 'actionname'
		   or actionAttribute.tag == 'animationname'):
			tableMid += '<td>' + actionAttribute.text + '</td>'

print(tableBegin + tableMid + tableEnd)
function getXmlText(filename, elementId)
{
    var xmlHTTP = new XMLHttpRequest();
    try
    {
    xmlHTTP.open("GET", filename, false);
    xmlHTTP.send(null);
    }
    catch (e) {
        window.alert("Unable to load the requested file.");
        return;
    }

    return xmlHTTP.responseText;
}

function getXMLDoc(xmlText)
{
    var xmlDoc;

    if (window.DOMParser)
    {
        parser = new DOMParser();
        xmlDoc = parser.parseFromString(xmlText, "text/xml");
    }
    else // Internet Explorer
    {
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = false;
        xmlDoc.loadXML(xmlText);
    }  
    return xmlDoc;
}
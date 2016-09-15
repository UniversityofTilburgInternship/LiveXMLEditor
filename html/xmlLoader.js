function loadFileToElement(filename, elementId)
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
        xmlDoc = parser.parseFromString(txt, "text/xml");
    }
    else // Internet Explorer
    {
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = false;
        xmlDoc.loadXML(txt);
    }  
    return xmlDoc;
}
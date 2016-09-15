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

function drawTablesForEachActionInXML()
{
    var xmlText = getXmlText("xml.xml", "test"),
    xmlDocument = $.parseXML(xmlText),
    $xml = $(xmlDocument),
    $actionElements = $xml.find("action");
    
    $actionElements.each(function () {
        var tableForThisActionElement = document.createElement("table");

        var row1 = tableForThisActionElement.insertRow(0);
        var row2 = tableForThisActionElement.insertRow(1);
        var row3 = tableForThisActionElement.insertRow(2);

        var cell1 = row1.insertCell(0);
        var cell2 = row2.insertCell(0);
        var cell3 = row3.insertCell(0);

        cell1.innerHTML = $(this).children('actionId').text();
        cell2.innerHTML = $(this).children('actionname').text();
        cell3.innerHTML = $(this).children('animationname').text();
        /*
        row1.insertCell($(this).children('actionId').text());
        row2.insertCell($(this).children('actionname').text());
        row3.insertCell($(this).children('animationname').text());
*/
        //find this action in the xml
        //find this element's children using .children, aka. properties
        //add THESE AS rows to tableFOrThisActionElement

        document.body.appendChild(tableForThisActionElement);


      //document.write($(this).children('actionId').text()); 
    });


           /*
            TODO: 
            Loop through the actions, create an table for each actions with its' rows being its' values.
            */
}


//JQuery function which iterates through child elements, excluding the specified mask from the result set.
$.fn.findChildrenWithExclude = function( selector, mask, result )
{
    result = typeof result !== 'undefined' ? result : new jQuery();
    this.children().each( function(){
        thisObject = jQuery( this );
        if( thisObject.is( selector ) ) 
            result.push( this );
        if( !thisObject.is( mask ) )
            thisObject.findExclude( selector, mask, result );
    });
    return result;
}


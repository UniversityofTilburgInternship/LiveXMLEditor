class htmlWriter():

	# Find a cleaner way to do this
  def getHeadHtml(self):
        return """<html>
                        <head>
                             <!-- Latest compiled and minified CSS -->
                            <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                            <!-- jQuery library -->
                            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
                            <!-- Latest compiled JavaScript -->
                            <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
                            <title>Action.xml content</title>
                        </head>
                    <body>
                     <script type="text/javascript">
                    function xml_http_post(url, data, callback) 
					{
                        var req = false;
                        try 
						{
                            // Firefox, Opera 8.0+, Safari
                            req = new XMLHttpRequest();
                        }
                        catch (e)
					    {
                            // Internet Explorer
                            try 
							{
                                req = new ActiveXObject("Msxml2.XMLHTTP");
                            }
                            catch (e) 
							{
                                try 
								{
                                    req = new ActiveXObject("Microsoft.XMLHTTP");
                                }
                                catch (e) 
								{
                                    alert("Your browser does not support AJAX!");
                                    return false;
                                }
                            }
                        }

                        req.open("POST", url, true);
                        req.onreadystatechange = function() 
						{
                            if (req.readyState == 4) 
							{
                                callback(req);
                            }
                        }
                        req.send(data);
                    }



                    function test_button()
				    {
                        var data = 1;           
                        xml_http_post("index.html", data, test_handle)
                    }

                    function test_handle(req) 
					{
                        var elem = document.getElementById('test_result')
                        elem.innerHTML =  req.responseText
                    }

                    </script>
					<span id="test_result">0</span>
					<input type=button onClick="test_button();" value="start" title="start">"""


  def getTailHtml(self):
      return "</body></html>"
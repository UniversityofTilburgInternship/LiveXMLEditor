<!DOCTYPE>

<html>

<head>
    <title>cose demo 676</title>

    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, maximum-scale=1">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

    <!-- Latest compiled JavaScript -->
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="http://cytoscape.github.io/cytoscape.js/api/cytoscape.js-latest/cytoscape.min.js"></script>

    <style>
        body {
            font-family: helvetica;
            font-size: 14px;
        }

        #cy {
            width: 80%;
            height: 100%;
            position: absolute;
            left: 260px;
            top: 0;
            z-index: 1;
        }

        h1 {
            color: white;
        }

        h2 {
            color: rgb(85, 85, 85);
        }

        .col-md-2 {
            position: absolute;
            z-index: 100;
            background-color: cadetblue;
            color: white;
            margin-top: -20px !important;
            padding-top: 0px !important;
            height: 100%;
        }
    </style>


</head>

<body>


<div class="col-md-2">
    <h1>Graph editor</h1>
    <h2 id="nodeName"></h2>
    <h3 id="nodeModifierHeader"></h3>
    <div class="form-group">
        <label for="actionName">action name:</label>
        <input type="text" class="form-control" id="actionName">
    </div>
    <div class="form-group">
        <label for="animationName">animation name:</label>
        <input type="text" class="form-control" id="animationName">
    </div>
    <div class="form-group">
        <label for="neighbours">neigbours:</label>
        <select class="form-control" id="neighbours">

        </select>
    </div>

    <button type="submit" class="btn btn-default">Save</button>
</div>

<h1>Graph</h1>
<div id="cy"></div>


</body>

<script>
    var cy = cytoscape({
        container: $('#cy')[0],

        boxSelectionEnabled: false,
        autounselectify: true,

        style: cytoscape.stylesheet()
                .selector('node')
                .css({
                    'content': 'data(name)',
                    'text-valign': 'center',
                    'color': 'white',
                    'text-outline-width': 2,
                    'text-outline-color': '#888'
                })
                .selector(':selected')
                .css({
                    'background-color': 'black',
                    'line-color': 'black',
                    'target-arrow-color': 'black',
                    'source-arrow-color': 'black',
                    'text-outline-color': 'black'
                }),

        elements: {
            nodes: {{!nodes}},
    edges: {{!edges}}
    },

    layout: {
        name: 'grid',
                padding
    :
        10
    }
    })
    ;

    cy.on('tap', 'node', function (evt) {
        var node = evt.cyTarget;
        $("#nodeName").html(node.data('name'));
        console.log('tapped ' + node.id());
    });


</script>


</html>

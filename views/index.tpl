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
    <script>
        $(document).ready(function () {
            $('#nodeEditor').submit(function (e) {
                $.ajax({
                    type: 'POST',
                    url: '/ajax',
                    data: $(this).serialize(),
                    success: function (response) {
                        $('#ajaxP').html(response);
                    }
                });
                e.preventDefault();
            });
        });
    </script>

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
                %for action in actions:
                <option value='{{action["data"]["name"]}}'>{{action["data"]["name"]}}</option>
                %end
            </select>
                <button>+</button>

            <div class="neighbours">

            </div>
        </div>
        <div class="form-group">
            <label for="modifiers">personality modifiers:</label>
            <select class="form-control" id="modifiers">
                %for personality in personalities:
                <option value='{{personality["data"]["name"]}}'>{{personality["data"]["name"]}}</option>
                %end
            </select>
        </div>
        <button type="submit" class="btn btn-default">Save</button>
</div>

<h1>Graph</h1>
<div id="cy"></div>


</body>

<script>
    var nodes = {{!nodes}};
    var edges = {{!edges}};
    var cy = cytoscape({
        container: $('#cy')[0],

        boxSelectionEnabled: false,
        autounselectify: true,

        style: cytoscape.stylesheet()
                .selector('node')
                .css({
                    'content': 'data(name)'
                })
                .selector('edge')
                .css({
                    'target-arrow-shape': 'triangle',
                    'width': 4,
                    'line-color': '#ddd',
                    'target-arrow-color': '#ddd',
                    'curve-style': 'bezier'
                })
                .selector('.highlighted')
                .css({
                    'background-color': '#61bffc',
                    'line-color': '#61bffc',
                    'target-arrow-color': '#61bffc',
                    'transition-property': 'background-color, line-color, target-arrow-color',
                    'transition-duration': '0.5s'
                }),

        elements: {
            nodes: nodes,
    edges: edges
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
        $("#actionName").val(node.data('name'));
        $("#animationName").val(node.data('animationname'));
        console.log('tapped ' + node.id());

        var neighboursSelectElement = document.getElementById('neighbours');

        $('.neighbours').empty();

        for(var i = 0; i < node.connectedEdges().length; i++)
        {
            var currentNodeName = node.connectedEdges()[i].target().data('name');

            if(currentNodeName != node.data('name'))
                $('.neighbours').append('<div class="col-md-8">' + currentNodeName + '' +
                        '</div> <div class="col-md-4">' +
                        '<button onclick="removeNeighbour('+ node.connectedEdges()[i].target().data("id")+ ', ' + node.id() +
                        ')">-</button></div> ');
        }
    });

    function removeNeighbour(neighbourId, rootId)
    {
        for (var i = 0; i < edges.length; i++)
        {
            if(edges[i].data.source == rootId && edges[i].data.target == neighbourId)
            {
                console.log(edges[i].data.id);

                var escapedEdgeId = edges[i].data.id;

                var edgeToRemove = cy.edges("edge[id='" + escapedEdgeId + "']");
                console.log('Edge to remove: ' + edgeToRemove);
                edgeToRemove.remove();

                break;
            }
        }
        sendNodeToDeleteToPython(neighbourId, rootId);

        //location.reload();
    }

    function sendNodeToDeleteToPython(neighbourToDelete, rootOfNeighbour)
    {
        $.ajax({
            type: 'POST',
            url: '/',
            data: {neighbourId: neighbourToDelete, rootId: rootOfNeighbour}
        });
    }


</script>


</html>

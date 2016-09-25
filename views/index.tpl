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
            color: rgb(85,85,85);
        }

        .col-md-2 {
            position: absolute;
            z-index: 100;
            background-color: cadetblue;
            color: white;
            margin-top: -20px !important;
            padding-top: 0px!important;
            height: 100%;
        }
    </style>
<<<<<<< HEAD

</head>

<body>
=======
    <script>

        $(function(){
    var cy = window.cy = cytoscape({
    container: document.getElementById('cy'),

    layout: {
    name: 'cose',
    idealEdgeLength: 100,
    nodeOverlap: 20
    },
    elements: {{ !res }},

    style: [{"selector":"core","style":{"selection-box-color":"#AAD8FF","selection-box-border-color":"#8BB0D0","selection-box-opacity":"0.5"}},{"selector":"node","style":{"width":"mapData(score, 0, 0.006769776522008331, 20, 60)","height":"mapData(score, 0, 0.006769776522008331, 20, 60)","content":"data(name)","font-size":"12px","text-valign":"center","text-halign":"center","background-color":"#555","text-outline-color":"#555","text-outline-width":"2px","color":"#fff","overlay-padding":"6px","z-index":"10"}},{"selector":"node[?attr]","style":{"shape":"rectangle","background-color":"#aaa","text-outline-color":"#aaa","width":"16px","height":"16px","font-size":"6px","z-index":"1"}},{"selector":"node[?query]","style":{"background-clip":"none","background-fit":"contain"}},{"selector":"node:selected","style":{"border-width":"6px","border-color":"#AAD8FF","border-opacity":"0.5","background-color":"#77828C","text-outline-color":"#77828C"}},{"selector":"edge","style":{"curve-style":"haystack","haystack-radius":"0.5","opacity":"0.4","line-color":"#bbb","width":"mapData(weight, 0, 1, 1, 8)","overlay-padding":"3px"}},{"selector":"node.unhighlighted","style":{"opacity":"0.2"}},{"selector":"edge.unhighlighted","style":{"opacity":"0.05"}},{"selector":".highlighted","style":{"z-index":"999999"}},{"selector":"node.highlighted","style":{"border-width":"6px","border-color":"#AAD8FF","border-opacity":"0.5","background-color":"#394855","text-outline-color":"#394855","shadow-blur":"12px","shadow-color":"#000","shadow-opacity":"0.8","shadow-offset-x":"0px","shadow-offset-y":"4px"}},{"selector":"edge.filtered","style":{"opacity":"0"}},{"selector":"edge[group=\"coexp\"]","style":{"line-color":"#d0b7d5"}},{"selector":"edge[group=\"coloc\"]","style":{"line-color":"#a0b3dc"}},{"selector":"edge[group=\"gi\"]","style":{"line-color":"#90e190"}},{"selector":"edge[group=\"path\"]","style":{"line-color":"#9bd8de"}},{"selector":"edge[group=\"pi\"]","style":{"line-color":"#eaa2a2"}},{"selector":"edge[group=\"predict\"]","style":{"line-color":"#f6c384"}},{"selector":"edge[group=\"spd\"]","style":{"line-color":"#dad4a2"}},{"selector":"edge[group=\"spd_attr\"]","style":{"line-color":"#D0D0D0"}},{"selector":"edge[group=\"reg\"]","style":{"line-color":"#D0D0D0"}},{"selector":"edge[group=\"reg_attr\"]","style":{"line-color":"#D0D0D0"}},{"selector":"edge[group=\"user\"]","style":{"line-color":"#f0ec86"}}],


    });
            cy.on('tap', 'node', function(evt){
                var node = evt.cyTarget;
                var nodeNameInForm = document.getElementById('nodeName');
                nodeNameInForm.innerHTML = node.data('name');

                console.log( 'tapped ' + node.id() );
            });
    });

    </script>
</head>

<body>
<h3 id="nodeName"></h3>
<h4 id="nodeModifierHeader"></h4>


>>>>>>> 4d11f28654b61aa40f784a13edda03835cf098d0


    <div class="col-md-2">
        <h1>Graph editor</h1>
        <h2 id="nodeName"></h2>
        <h3 id="nodeModifierHeader"></h3>
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
            padding: 10
        }
    });

    cy.on('tap', 'node', function(evt){
        var node = evt.cyTarget;
        $( "#nodeName" ).html(node.data('name'));
        console.log( 'tapped ' + node.id() );
    });


</script>


</html>

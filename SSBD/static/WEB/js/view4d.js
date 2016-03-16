 <script>
    var bdml_id = {{  bdml_id  }};
    var time_t = {{  t }};
    var last_t = 0;
    var base_url = "/SSBD/";
    var ssbd_url;
    var scale_url = base_url+"api/v1/scale/"+bdml_id+"/";

    ssbd_url = base_url+"BDML/vertices/"+bdml_id+"/t/"+time_t+"/etype/";
    console.log(ssbd_url);
    var param = "?callback=?"; // for allowing cross domain query

    var camera, controls, scene, renderer;
    var geometry;
    var line=[];
    var sphere=[];
    var points;
    var basic_material;
    var lambert_material;
    var mouseX = 300;
    var mouseY = 300;
    var line_error = 0;
    var point_error = 0;
    var sphere_error = 0;
    var j = 0; // index for line, sphere
    var camx = {{ cam_x }};
    var camy = {{ cam_y }};
    var camz = {{ cam_z }};
    var avgx = {{ avgx }};
    var avgy = {{ avgy }};
    var avgz = {{ avgz }};
    var xmax = {{ xmax }};
    var ymax = {{ ymax }};
    var zmax = {{ zmax }};
    var xmin = {{ xmin }};
    var ymin = {{ ymin }};
    var zmin = {{ zmin }};
    var xscale = {{ xscale }};
    var yscale = {{ yscale }};
    var zscale = {{ zscale }};
    var scaleup = {{ scaleup }};
    var tunit = '{{ tunit }}';
    var tscale = {{ tscale }};
//    console.log("num_components="+num_components+" num_entities="+num_entities)
//    alert("num_components="+num_components+" num_entities="+num_entities)
// max_tp is the maximum number of time points.
// Currently in order to make the viewer work for Kimura data, it is set to use a hard code time scale of 0.01, i.e. 1/100 
// so for time pt 100, we call it timept 1 instead in the actual code.
// scaletime is recorded in each of the json files, so that it provide a record that the timept was shrunk 1/100 times.
    if (max_tp > 10000){
        var scaletime = 0.01;
    }
    else {
        var scaletime = 1;
    }
        
//    var progresspct = 40;

    function updateProgressBar(){
        filecount++;
//        console.log("filecount=%d", filecount);
        progresspct = Math.floor( filecount / totalnumfile * 100 );
        $('#progressbar').progressbar({value : progresspct});
//        console.log("filecount=%d, totalnumfile=%d,  progresspct=%d", filecount, totalnumfile, progresspct);
        var msg = "LOADING ...... "+filecount+"/"+totalnumfile+" ("+progresspct+"% )";
//        console.log(msg)
        $( "#messagetxt" ).val( msg );
        if (progresspct == 100){
            $('#progressbar').progressbar({complete: function(){$("#messagetxt").val("LOADING 100% Complete")}})
        }
        return progresspct;
    }

    function SSBDviewStart(){
       //grab our container div
       var container = document.getElementById("container");
       if ( ! Detector.webgl ) {
          var warning = Detector.getWebGLErrorMessage();
          alert("Cannot detect WebGL, please enable WebGL or use another browser");
          document.getElementById('container').appendChild(warning);

       }
       // create a Three.js renderer and add it to container div
       renderer = new THREE.WebGLRenderer();
       renderer.setSize(container.offsetWidth, container.offsetHeight)
       container.appendChild(renderer.domElement);

       // create a new Three.js scene
       scene = new THREE.Scene();


       //creat a camera and add it to the scene
       camera = new THREE.PerspectiveCamera(45, container.offsetWidth/container.offsetHeight, 1, 6000);


       controls = new THREE.TrackballControls(camera, renderer.domElement);
       controls.rotateSpeed = 0.8;
       controls.zoomSpeed = 1.2;
       controls.panSpeed = 0.8;
       controls.noZoom = false;
       controls.noPan = false;
       controls.staticMoving = false;
       controls.dynamicDampingFactor = 0.5;
       controls.CAMERA_RADIUS =20;

       if( camz == 0 ){
           camz = 500;
       }
//       controls.target.set(camx,cam, camz);
       var midx = ((xmax-xmin)/2);
       var midy = ((ymax-ymin)/2);
       var midz = ((zmax-zmin)/2);
//       controls.target.set(midx*xscale*scaleup,midy*yscale*scaleup,midz*zscale*scaleup);
       controls.target.set(midx*scaleup,midy*scaleup,midz*scaleup);
       controls.keys = [ 65, 83, 68 ]; // [ rotateKey, zoomKey, panKey ]
       controls.addEventListener( 'change', render );

       if ({{ zscale }} == 0){
            zscale = 1;
       }

// LIGHT
	   var light = new THREE.PointLight(0xffffff);
//	   alert("camx="+camx+" camy="+camy+" camz="+camz);
	   light.position.set(camx*2, camy*2, camz*10);
       scene.add(light);

       // need to add an ambient light
	   //  for ambient colors to be visible
	   // make the ambient light darker so that
	   //  it doesn't overwhelm (like emmisive light)
	   var light2 = new THREE.AmbientLight(0x333333);
	   light2.position.set( light.position );
	   scene.add(light2);
       resetCamera();
       scene.add(camera);
       makeGrid();
       makeCoordinateArrows();


       line_error = SSBDviewDrawlines();
       point_error = SSBDviewDrawpoints();
       sphere_error = SSBDviewDrawspheres();
//       VisibleLines();
       animate();

    function resetCamera(){
    //    camera.position.set (camx*2,camy*2,camz*2);
        camera.position.set (camx,camy,camz*7);
        controls.target.set(camx, camy, camz);
    }

/** INNACCESSIBLE OBJECTS **/

	///////////////////
	//   GUI SETUP   //
	///////////////////

	var gui = new dat.GUI({ autoPlace: true });
    document.getElementById('gui-container').appendChild(gui.domElement);
	var parameters =
	{
		resetCam:  function() { resetCamera(); },
        rotatevisible : false,
        gridvisible : false,
        axisvisible : true,
        colour : "#ffffff",
        material: "Lambert",
        objectvisible : true,
//        scalefactor: scaleup,
	};

	// GUI -- parameters
	gui.add( parameters, 'resetCam' ).name("Reset Camera");
    var rotationVisibility = gui.add( parameters, 'rotatevisible').name('Toggle Rotate').listen();
    var gridVisibility = gui.add( parameters, 'gridvisible').name('Toggle Grid').listen();
    var axisVisibility = gui.add( parameters, 'axisvisible').name('Toggle Axis').listen();
//    var objectVisibility = gui.add( parameters, 'objectvisible').name('Toggle Objects').listen();
//    var objectColour = gui.addColor( parameters, 'colour').name('Colour').listen();
//    var objectMaterial = gui.add( parameters, 'material', [ "Lambert", "Wireframe" ] ).name('Material Type').listen();
/*
    var timeMin = gui.add( parameters, 'timept_min').min({{ min_t }}).max({{ max_t}}).step(1).name('Time Pt from').listen();
    var timeMax = gui.add( parameters, 'timept_max').min({{ min_t }}).max({{ max_t}}).step(1).name('Time Pt to').listen();
*/

    rotationVisibility.onChange(function(gvalue){
            updateRotate();
    });

    gridVisibility.onChange(function(gvalue){
        updateGrid();
    });

    axisVisibility.onChange(function(avalue){
        updateAxis();
    });
/*
    objectVisibility.onChange(function(avalue){
        updateObject();
    });
*/
/*
    objectColour.onChange(function(cvalue){
            updateObjectColour();
    });
*/
/*
    objectMaterial.onChange(function(mvalue){
        updateSphereObject();
    });
*/
    function removeObject(){
      if ( line  != [] ){
         line.forEach(function(lvalue){
//                console.log(lvalue);
                scene.remove(lvalue);
         });
      } // end if line
      if ( sphere !== []){
          for(i=0; i<sphere.length; i=i+1) {
//            console.log("sphere.length="+sphere.length);
//            console.log("i="+i);
            scene.remove(sphere[i]);
          }
      }
      if ( points ){
            scene.remove(points);
      }
      render();
    } // end removeObject

    function updateObject(){
      if ( line  != [] ){
         line.forEach(function(lvalue){
                console.log(lvalue);
                lvalue.visible = parameters.objectvisible;
         });
      } // end if line
      if ( sphere !== []){
          for(i=0; i<sphere.length; i=i+1) {
            console.log("sphere.length="+sphere.length);
            console.log("i="+i);
            sphere[i].visible = parameters.objectvisible;
          }
      }
      if ( points ){
            points.visible = parameters.objectvisible;
      }
            render();
    } // end updateObject

    function updateObjectColour(){
      if ( line  != [] ){
          line.forEach(function(lvalue){
               console.log(lvalue);
               lvalue.material.color.setHex( parameters.colour.replace("#", "0x"));
           });
      }

      if ( sphere !== []){
          for(i=0; i<sphere.length; i=i+1) {
            console.log("sphere.length="+sphere.length);
            console.log("i="+i);
            sphere[i].material.color.setHex( parameters.colour.replace("#", "0x"));
          }
      }
      if ( points ){
            points.material.color.setHex( parameters.colour.replace("#", "0x"));
      }
      render();
    }

    function updateSphereObject(){
           var newMaterial;
           var matvalue = parameters.material;
           var matcolour = parameters.colour.replace("#","0x");
           console.log(matcolour)

        if ( sphere !== []){
           if (matvalue == "Wireframe"){
               for(i=0; i<sphere.length; i=i+1) {
                   sphere[i].material = basic_material;
                   sphere[i].material.color.setHex( matcolour );
                   sphere[i].material.needsUpdate = true;
               }
           } // end if Basic
	       else if (matvalue == "Lambert"){
                   for(i=0; i<sphere.length; i=i+1) {
                      sphere[i].material = lambert_material;
                      sphere[i].material.color.setHex( matcolour );
                      sphere[i].material.needsUpdate = true;
                   }
           } // end if lambert
//		        newMaterial = new THREE.MeshBasicMaterial( { wireframe: true } );
//                sphere.material = basic_material;
           render();
        } // end if sphere
    } // end updateSphereObject

var cam_rotation = false;
function updateRotate(){
    cam_rotation = parameters.rotatevisible;
    render();
}

function rotation_cam(){
        var uscale;

        var timer = Date.now() * 0.0004;
//      camera.position.x = 1000*Math.cos(timer);
        var r = Math.sqrt(Math.pow((camx-avgx),2)+Math.pow((camy-avgy), 2));
        if(xscale < zscale){
            uscale = xscale;
        }
        else {
             uscale = zscale;
        }
        camera.position.x = (camx+r*Math.cos(timer)*uscale*scaleup*3);
//        camera.position.x = (controls.position.x+r*Math.cos(timer)*uscale*scaleup*3);
//      camera.position.y += (- mouseY - camera.position.y)*0.05;
        camera.position.z = (camz+r*Math.sin(timer)*uscale*scaleup*3);
//        camera.position.z = (controls.position.z+r*Math.sin(timer)*uscale*scaleup*3);
        camera.lookAt(controls.target);
} // end rotation_cam

/* GRID */
var grid;
function makeGrid() {
        var gridGeometry = new THREE.Geometry();
        var i;
        var xmax = {{ xmax }};
        var ymax = {{ ymax }};
        var xmin = {{ xmin }};
        var ymin = {{ ymin }};
//        var int = ( xmax - xmin )*xscale*scaleup/10;
//        var xmargin = xmax-xmin;
//        var ymargin = ymax-ymin;
//        var gridminx = (xmin-xmargin)*xscale*scaleup;
//        var gridmaxx = (xmax+xmargin)*xscale*scaleup;
//        var gridminy = (ymin-ymargin)*yscale*scaleup;
//        var gridmaxy = (ymax+ymargin)*yscale*scaleup;
        var int = ( xmax - xmin )/10;
        var xmargin = xmax-xmin;
        var ymargin = ymax-ymin;
        var gridminx = (xmin-xmargin);
        var gridmaxx = (xmax+xmargin);
        var gridminy = (ymin-ymargin);
        var gridmaxy = (ymax+ymargin);
        console.log("gridminx="+gridminx+" gridminy="+gridminy+" int="+int);
        for(i=gridminx; i<gridmaxx; i=i+int) {
            gridGeometry.vertices.push( new THREE.Vector3( i, gridminy, 0 ) );
            gridGeometry.vertices.push( new THREE.Vector3( i, gridmaxy,  0 ) );
        }
        for(i=gridminy; i<gridmaxy; i=i+int) {
            gridGeometry.vertices.push( new THREE.Vector3( gridminx, i, 0 ) );
            gridGeometry.vertices.push( new THREE.Vector3( gridmaxx, i, 0 ) );
        }
        var gridMaterial = new THREE.LineBasicMaterial( { color: 0xBBBBBB } );
        grid = new THREE.Line(gridGeometry, gridMaterial, THREE.LinePieces);
        grid.visible = false;
        scene.add( grid );
        render();
        return grid;
}

function updateGrid(){
        grid.visible = parameters.gridvisible;
        render();
}

/* COORDINATE ARROWS */
    var coordinateArrows;

    function makeCoordinateArrows() {
        coordinateArrows = new THREE.Object3D();
        var org = new THREE.Vector3( 0, 0, 0);

        var dir = new THREE.Vector3( 0, 0, 1);
        coordinateArrows.add( new THREE.ArrowHelper( dir, org, 8, 0x0000FF ) ); // Blue = z
        dir = new THREE.Vector3( 0, 1, 0 );
        coordinateArrows.add( new THREE.ArrowHelper( dir, org, 8, 0x00FF00 ) ); // Green = y
        dir = new THREE.Vector3( 1, 0, 0 );
        coordinateArrows.add( new THREE.ArrowHelper( dir, org, 8, 0xFF0000 ) ); // Red = x
        scene.add( coordinateArrows );
        render();
        return coordinateArrows;
    }

    function updateAxis(){
        coordinateArrows.traverse(function (child){
        child.visible = parameters.axisvisible;
        });
        render();
    }


    function SSBDviewDrawlines(){
           // ** Global variable ** entity is an array of objects {id: entityid, time: t, line: l}
           entity = new Array();

//           var material = new THREE.LineBasicMaterial( {color: 0xffffff, opacity: 1, lineWidth:3, visible:true})
           var material = new THREE.LineBasicMaterial( {color: 0xffffff, opacity: 1, lineWidth:3})

           var lastid = 0;
//           var datatime = 0;
           var entityid=0;
           var listjsonstring = 'data/ssbd_id_'+bdml_id+'/line.json';
//           alert("listjsonstring="+listjsonstring);
           var jsonlistfile = "{%  static 'WEB/'%}"+listjsonstring;
//           alert("jsonlistfile="+jsonlistfile);
           $.getJSON(jsonlistfile, function(filedata) {
               console.log("filedata=%O", filedata)
               filestoload=filedata.filelist;
               console.log("filestoload=%O", filestoload)
               totalnumfile=totalnumfile+filestoload.length;
               console.log("totalnumfile=%O", totalnumfile)
           }) // getJSON
           .done(function(){
               while(filestoload.length!=0) {
//                 console.log("filestoload.length=%d", filestoload.length);
                 loadstaticlinefiles();
//                 VisibleLines();
               }
           }) // end .done
           .error(function(jqXhr, textStatus, error) {
                console.log("ERROR: " + textStatus + ", " + error);
           }); // end error

           function loadstaticlinefiles(){
             var k = 0; // line index
             var file = filestoload.shift();
             console.log("file=%s", file);
             var a = $.getJSON(file, function(data) {
             var entityid = data.vertices[0];
             var datatime = data.vertices[5];
             console.log("Json has data property. entityid="+entityid);
             console.log("Json has data property. datatime="+datatime);
             if (data.hasOwnProperty('scale_array')){
                 var scale_array = JSON.parse(data.scale_array);
                 scaletime = scale_array[5];
                 console.log("Json has scale_array property. scaletime="+scaletime);
             }
             else{
                 scaletime = 1;
             }
//             alert("scale_array="+scale_array)
//             alert("scale_array[5]="+scale_array[5])
//             console.log("loadstaticlinefiles.scaletime="+scaletime)
             if (data.hasOwnProperty('timept')){
                 var lntimept = parseInt(data.timept);
//                 console.log("Json has timept property. lntimept="+lntimept);
             }
             else{
                     lntimept = datatime/tscale;
//                     console.log("Json has NO timept property. lntimept="+lntimept);
             }
//               console.log("entityid="+entityid+" data.vertices[0]="+data.vertices[0]+" datatime="+datatime)
             geometry = new THREE.Geometry();
             geometry.dynamic = true;
             geometry.verticesNeedUpdate = true;
             geometry.normalsNeedUpdate = true;
//               console.log("locadstaticfiles->getJSON->time_t="+time_t);
             if(data.vertices !== "error"){
               // data array is in the form [entity_id, coord_id,x,y,z,t ... ]
//                    console.log("locadstaticfiles->getJSON->j=%d",j);
//                    entity[datatime/tscale]=new Array();
                    entity[lntimept]=new Array();
                    for(var i= 0, len = data.vertices.length; i < len; i=i+6){
                        // if it is the same line entity, keep ending vertices
//                       console.log("entityid=%d, data.vertices[%d]=%d", entityid, i, data.vertices[i])
                       if (data.vertices[i] == entityid){
                              geometry.vertices.push(new THREE.Vector3(
                                    (data.vertices[i+2]),
                                    (data.vertices[i+3]),
                                    data.vertices[i+4]));
//                              datatime = data.vertices[i+5]
                        }
                        else {
                           // if it is a different entity, add the current vertices to a new line
                           // and add to the entity[j]; start a new line with a new geometry, update entityid
                              var dataline = new THREE.Line(geometry, material);
                            // Adding the new line into an array of lines entity
                        //finish ending a new line entity[j], now start a new line.
                              geometry = new THREE.Geometry();
                              geometry.vertices.push(new THREE.Vector3(
                                (data.vertices[i+2]),
                                (data.vertices[i+3]),
                                data.vertices[i+4]));
//                              datatime = data.vertices[i+5]
                              dataline.visible = false;
                              entity[lntimept][k] = {id:entityid, time:datatime, line:dataline};
                            //starting a new line here, reset entityid
                              entityid = data.vertices[i];
                            // show it onscreen
//                              console.log("entity[%d][%d].line=%f", lntimept, k, entity[lntimept][k]);
                              scene.add(entity[lntimept][k].line);
                           k=k+1;
                        } // end else
                        // if there is only 1 line!! 
                        if(k==0) {
                              var dataline = new THREE.Line(geometry, material);
                              dataline.visible = false;
                              entity[lntimept][k] = {id:entityid, time:datatime, line:dataline};
                              scene.add(entity[lntimept][k].line);
                        }
                        //finish ending a new line entity[j]
                    }; // end for loop
                 } //end if vertices length
                 else{
                    line_error = 1;
                 }
              } // function data
           ) // getJSON ssdb_url
           .fail(function(){
                  console.log("error on getJSON fail")
           })
//           return {"line_error" : line_error}
            .done(function(){
                updateProgressBar();
            })
          }; // end of loadstaticfiles

      }; // end of SSBDviewDrawlines


       function SSBDviewDrawpoints(){
       // * Global variables * entitypt is an array of objects {id: entityptid, time: t, point: l}
           entitypt = new Array();

           var material = new THREE.ParticleBasicMaterial( {color: 0xffffff, size:1})

           var lastid = 0;
//           var datatime = 0;
           var entityptid=0;
           var listjsonstring = 'data/ssbd_id_'+bdml_id+'/point.json';
//           alert("listjsonstring="+listjsonstring);
           var jsonlistfile = "{%  static 'WEB/'%}"+listjsonstring;
//           alert("jsonlistfile="+jsonlistfile);
           $.getJSON(jsonlistfile, function(filedata) {
//               console.log("filedata=%O", filedata)
               filestoload=filedata.filelist;
//               console.log("filestoload=%O", filestoload)
           }) // getJSON
           .done(function(){
               time_t = min_t;
//               console.log("Original filestoload.length=%d", filestoload.length);
               totalnumfile=totalnumfile+filestoload.length;
               while(filestoload.length!=0) {
//                 console.log("filestoload.length=%d", filestoload.length);
                 loadptstaticfiles(6);
               }
//               console.log("done loading");
           }) // end .done
           .error(function(jqXhr, textStatus, error) {
                console.log("ERROR: " + textStatus + ", " + error);
           });
           function loadptstaticfiles(interval){
             var file = filestoload.shift();
             var a = $.getJSON(file, function(data) {
                            var pttimept = parseInt(data.timept);
                            var entityptid = data.vertices[0];
                            var datatime = data.vertices[5];
                            if(data.vertices !== "error"){
                            // data array is in the form [entity_id, coord_id,x,y,z,t ... ]
                                // ** Global variable ** entitypt for storing entity points
                                entitypt[pttimept]=new Array();
//                                visibilitypt[pttimept] = false;
                                var geometry = new THREE.Geometry();
                                var datapoint = new THREE.ParticleSystem(geometry, material);
                                var j=0; // point index
                                for(var i= 0, len = data.vertices.length; i < len; i=i+interval){
                                    geometry.dynamic = true;
                                    geometry.verticesNeedUpdate = true;
                                    geometry.normalsNeedUpdate = true;
                                    geometry.vertices.push(new THREE.Vector3(
                                        (data.vertices[i+2]),
                                        (data.vertices[i+3]),
                                        data.vertices[i+4])
                                    );
                                    // ToDo: how to automatically calculate the size??
                                    datapoint.material.size=0.01;
                                    datapoint.visible = false;
//                                    datapoint.visible = function(pttimept){ return visibilitypt[pttimept]};
                                    entityptid = data.vertices[i];
                        // Adding new point into an array of point entity
                                    entitypt[pttimept][j] = {id:entityptid, time:datatime, point:datapoint};
//                                    console.log("entitypt[%d][%d]=%0", pttimept, j, entitypt[pttimept][j]);
                        //starting a new pt here, reset entityid
                        // show it onscreen
//                                    scene.add(entitypt[pttimept][j].point);
                        //finish ending a new point entity[j]
                                    j++;
                                }; // end for loop
                                // show it onscreen
                                scene.add(datapoint);
                            } //end if vertices length
                            else{
                                point_error = 1;
                            }
                         } // end function data
                        ) // getJSON ssdb_url
                        .done(function(){
                            updateProgressBar();
                        }) // .done function data
                        .fail(function(){
                            console.log("error on getJSON fail")
                        })
          }; // end of loadptstaticfiles

    }; // end of SSBDviewDrawpoints

       function SSBDviewDrawspheres(){
       // * Global variables * entitySph is an array of objects {id: entityptid, time: t, sphere: l}
           entitySph = new Array();

        // checking number of entities read
//           var count_entities = 0;

           // Default segments and rings size
//           var segments = 4, rings = 4;
           var segments = 5, rings = 5;
           // trying to be adaptive on segments and ring size based on the number of time points.
           // ToDo: It should based on the number of entities
           if (num_entities < 5000) {
               segments = 8;
               rings = 8;
           } // end if < 70
           if (num_entities < 2000) {
                   segments = 16;
                   rings = 16;
           } // end if < 50

           var basic_material = new THREE.MeshBasicMaterial( {color: 0xffffff, wireframe: true, transparent: true} );
           var lambert_material = new THREE.MeshLambertMaterial( {color: 0xffffff, opacity: 1, shininess:30} );
           var pt_material = new THREE.ParticleBasicMaterial( {color: 0xffffff, size:1})
//           var sphere_material = basic_material;
           var sphere_material = lambert_material;

           var lastid = 0;
//           var j = 0; // time pt index
//           var datatime = 0;
           var entitySphid=0;
           var listjsonstring = 'data/ssbd_id_'+bdml_id+'/sphere.json';
//           alert("listjsonstring="+listjsonstring);
           var jsonlistfile = "{%  static 'WEB/'%}"+listjsonstring;
//           alert("jsonlistfile="+jsonlistfile);
           $.getJSON(jsonlistfile, function(filedata) {
//               console.log("filedata=%O", filedata)
               filestoload=filedata.filelist;
//               console.log("filestoload=%O", filestoload)
           }) // getJSON
           .done(function(){
               time_t = min_t;
               totalnumfile=totalnumfile+filestoload.length;
               console.log("Original filestoload.length=%d", filestoload.length);
               while(filestoload.length!=0) {
                 console.log("filestoload.length=%d", filestoload.length);
//                 console.log("count_entities=%d", count_entities);
                 if(num_components < 25000){
                     console.log("drawing sphere")
                     loadsphstaticfiles();
                 }
                 else{
                     console.log("drawing pt")
                   loadsphptstaticfiles(7);
                 }
               }
               console.log("done loading");
           }) // end .done
           .error(function(jqXhr, textStatus, error) {
                console.log("ERROR: " + textStatus + ", " + error);
           });
           function loadsphstaticfiles(){
             var file = filestoload.shift();
               console.log("file=%s", file);
             var a = $.getJSON(file, function(filedata) {
//                        console.log("filedata=%0", filedata);
                        data=filedata; })
                        .done(function(){
//                            console.log("data=%0", data);
//                            console.log("data[timept]="+data["timept"]);
//                            console.log("data.timept="+data.timept);
//                            console.log("assigning to pttimept")
                            var sphtimept = parseInt(data.timept);
//                            console.log("sphtimept=%d", sphtimept);
                            var entitySphid = data.vertices[0];
                            var datatime = data.vertices[5];
//                          console.log("entityid=%d, data.vertices[0]=%d", entityid, data.vertices[0])
//                            console.log("entityptid="+entityptid+" data.vertices[0]="+data.vertices[0]+" datatime="+datatime)
                            group = new THREE.Object3D();
                            totalgeometry = new THREE.Geometry();
//                          console.log("locadstaticfiles->getJSON->time_t="+time_t)
//                          console.log("data.vertices="+data.vertices);
                            if(data.vertices !== "error"){
                                // ** Global variable ** entitypt for storing entity points
                                entitySph[sphtimept]=new Array();
                                var j=0; // sphere index
                             // data array is in the form [entity_id, coord_id,x,y,z,t,r ... ]
                                console.log('vertices.length='+data.vertices.length);
//                                count_entities = count_entities+data.vertices.length/7;
//                                console.log('count_entities='+count_entities);
                                for(var i= 0, len = data.vertices.length; i < len; i=i+7){
                                    var sphere_geometry = new THREE.SphereGeometry(data.vertices[i+6], segments, rings) 
                                    var sphere = new THREE.Mesh(sphere_geometry,  sphere_material);
//                                var sphere = new THREE.Mesh(new THREE.SphereGeometry(data.vertices[i+6], segments, rings), sphere_material);
//                                    sphere.position.x.copy(data.vertices[i+2]);
//                                    sphere.position.y.copy(data.vertices[i+3]);
//                                    sphere.position.z.copy(data.vertices[i+4]);
                                    sphere.position.x =  data.vertices[i+2];
                                    sphere.position.y =  data.vertices[i+3];
                                    sphere.position.z =  data.vertices[i+4];
                                    sphere.radius =  data.vertices[i+6];
                                    sphere.wireframe = 1;
                                    sphere.visible = false;
//                                    datapoint.visible = function(pttimept){ return visibilitypt[pttimept]};
                                    entitySphid = data.vertices[i];
                        // Adding new point into an array of point entity
                        // Todo : inefficient to copy sphere[j] into entitySph. Extend sphere to incorporate time and id will be better.
                                    entitySph[sphtimept][j] = {id:entitySphid, time:datatime, sphere:sphere};
//                                    console.log("entitySph[%d][%d]=%0", sphtimept, j, entitySph[sphtimept][j]);
                        //starting a new pt here, reset entityid
                        // show it onscreen
//                                    THREE.GeometryUtils.merge(totalgeometry, entitySph[sphtimept][j].sphere, 0);
                                    group.add(entitySph[sphtimept][j].sphere)
//old deleteable                                    scene.add(entitySph[sphtimept][j].sphere);
                        //finish ending a new point entity[j]
                                    j++;
                                }; // end for loop
                                // show it onscreen
                                scene.add(group);
//                                scene.add(new THREE.Mesh(totalgeometry, sphere_material));
                                updateProgressBar();
                            } //end if vertices length
                            else{
                                point_error = 1;
                            }
                        } // .done function data
                        ) // getJSON ssdb_url
                        .fail(function(){
//                            console.log("error on getJSON fail")
                        })
          }; // end of loadptstaticfiles
           function loadsphptstaticfiles(interval){
             var file = filestoload.shift();
             console.log("file=%s", file);
             var material = new THREE.ParticleBasicMaterial( {color: 0xffffff, size:1})
             var a = $.getJSON(file, function(data) {
                            var pttimept = parseInt(data.timept);
                            var entityptid = data.vertices[0];
                            var datatime = data.vertices[5];
                            if(data.vertices !== "error"){
                            // data array is in the form [entity_id, coord_id,x,y,z,t ... ]
                                // ** Global variable ** entitypt for storing entity points
                                entitypt[pttimept]=new Array();
//                                visibilitypt[pttimept] = false;
                                var geometry = new THREE.Geometry();
                                var datapoint = new THREE.ParticleSystem(geometry, material);
                                var j=0; // point index
                                console.log('data.vertices.length='+data.vertices.length);
//                                count_entities = count_entities+data.vertices.length/7;
                                for(var i= 0, len = data.vertices.length; i < len; i=i+interval){
                                    geometry.dynamic = true;
                                    geometry.verticesNeedUpdate = true;
                                    geometry.normalsNeedUpdate = true;
                                    geometry.vertices.push(new THREE.Vector3(
                                        (data.vertices[i+2]),
                                        (data.vertices[i+3]),
                                        data.vertices[i+4])
                                    );
                                    // ToDo: how to automatically calculate the size??
                                    datapoint.material.size=0.01;
                                    datapoint.visible = false;
//                                    datapoint.visible = function(pttimept){ return visibilitypt[pttimept]};
                                    entityptid = data.vertices[i];
                        // Adding new point into an array of point entity
                                    entitypt[pttimept][j] = {id:entityptid, time:datatime, point:datapoint};
//                                    console.log("entitypt[%d][%d]=%0", pttimept, j, entitypt[pttimept][j]);
                        //starting a new pt here, reset entityid
                        // show it onscreen
//                                    scene.add(entitypt[pttimept][j].point);
                        //finish ending a new point entity[j]
                                    j++;
                                }; // end for loop
                                // show it onscreen
                                scene.add(datapoint);
                            } //end if vertices length
                            else{
                                point_error = 1;
                            }
                         } // end function data
                        ) // getJSON ssdb_url
                        .done(function(){
                            updateProgressBar();
                        }) // .done function data
                        .fail(function(){
                            console.log("error on getJSON fail")
                        })
          }; // end of loadsphptstaticfiles
    }; // end of SSBDviewDrawSpheres

        function VisibleLines(){
        // switching everything off
           time_r = time_t;
//           console.log("VisibleLines: time_r="+time_r+"; time_t="+time_t);

//           console.log("VisibleLines false last_t=%d", last_t);
           if (last_t !== time_t) {
//               console.log("Checking1 typeof entity[%d]=%0 ...", time_r, entity[time_r]);
              if (typeof entity[last_t] !== "undefined") {
//                console.log("VisibleLines1 before if entity[%d].length=%d",last_t,entity[last_t].length);
                if (entity[last_t].length !== null) {
//                   console.log("Visibleline2 entity[%d].length=%d",time_r,entity[time_r].length);
                   for (var i = 0; i < entity[last_t].length; i++) {
//                     console.log("VisibleLines3 false entity[%d]=%0",i,entity[i]);
                     entity[last_t][i].line.visible = false;
                   } // end for
                } // end if length
              } // end if typeof
//              console.log("Checking2 typeof entitypt[%d]=%0 ...", time_r, entitypt[time_r]);
              if (typeof entitypt[last_t] !== "undefined") {
//                console.log("VisiblePoints1 before if entitypt[%d].length=%d",time_r,entitypt[time_r].length);
                if (entitypt[last_t].length !== null) {
//                   console.log("VisiblePoints2 entitypt[%d].length=%d",time_r,entitypt[time_r].length);
//                   console.log("Checking3 typeof entitypt[%d]=%0 ...", last_t, entitypt[last_t]);
                   if (typeof entitypt[last_t] !== "undefined"){
//                        visibilitypt[last_t] = false;
//                       console.log("VisiblePoints3 entitypt[%d].length=%d",last_t,entitypt[last_t].length);
                       for (var i = 0; i < entitypt[last_t].length; i++) {
//                         console.log("Entering for loop with i=%d", i)
//                         console.log("VisiblePoints4 false entitypt[%d][%d].point.visible =%s",last_t,i,entitypt[last_t][i].point.visible.valueOf());
                         entitypt[last_t][i].point.visible = false;
//                         console.log("VisiblePoints5 false entitypt[%d][%d].point.visible =%s",last_t,0,entitypt[last_t][0].point.visible.valueOf());
                       }// end for
//                       console.log("finishing for loop")
                   }// end if typeof
                } // end if length
              } // end if typeof
              if (typeof entitySph[last_t] !== "undefined") {
//                console.log("VisiblePoints1 before if entitypt[%d].length=%d",time_r,entitypt[time_r].length);
                if (entitySph[last_t].length !== null) {
//                   console.log("VisiblePoints2 entitypt[%d].length=%d",time_r,entitypt[time_r].length);
//                   console.log("Checking3 typeof entitypt[%d]=%0 ...", last_t, entitypt[last_t]);
                   if (typeof entitySph[last_t] !== "undefined"){
//                        visibilitypt[last_t] = false;
//                       console.log("VisiblePoints3 entitypt[%d].length=%d",last_t,entitypt[last_t].length);
                       for (var i = 0; i < entitySph[last_t].length; i++) {
//                         console.log("Entering for loop with i=%d", i)
//                         console.log("VisibleSphere false entitySph[%d][%d].sphere.visible =%s",last_t,i,entitySph[last_t][i].sphere.visible.valueOf());
                         entitySph[last_t][i].sphere.visible = false;
//                           console.log("VisibleSphere2 false entitySph[%d][%d].sphere.visible =%s",last_t,i,entitySph[last_t][i].sphere.visible.valueOf());
//                         console.log("VisiblePoints5 false entitypt[%d][%d].point.visible =%s",last_t,0,entitypt[last_t][0].point.visible.valueOf());
                       }// end for
//                       console.log("finishing for loop")
                   }// end if typeof
                } // end if length
              } // end if typeof
           } // end if only make invisible if last_t is not time_t
//           console.log("Checking4 typeof entity[%d]=%0 ...", time_r, entity[time_r]);
           if (typeof entity[time_r] !== "undefined") {
//               console.log("VisibleLines4 before if entity[%d].length=%d",time_r,entity[time_r].length);
               if (entity[time_r].length !== null) {
                   for (var i = 0; i < entity[time_r].length; i++) {
//                       console.log("VisibleLines5 true entity[%d][%d]=%O",time_r,i,entity[time_r][i]);
                       entity[time_r][i].line.visible = true;
//                   console.debug("setting true for visible for loop entity["+0+"]['line].geometry.vertices=%O",entity[0].line.geometry.vertices);
                   } // end for
               } // end if length
           } // end if typeof
//           console.log("Checking5 typeof entitypt[%d]=%0 ...", time_r, entitypt[time_r]);
           if (typeof entitypt[time_r] !== "undefined") {
//               console.log("VisiblePoints false entitypt[%d].point.length=%d",time_r,entitypt[time_r].point.length);
                if (entitypt[time_r].length !== null) {
//                    visibilitypt[time_r] = true;
//                    console.log("visibilitypt[%d]=%s",time_r, visibilitypt[time_r]);
                   for (var i = 0; i < entitypt[time_r].length; i++) {
//                       console.log("Entering for loop with i=%d", i)
//                       console.log("VisiblePoints6 false entitypt[%d][%d].point.visible =%s",time_r,i,entitypt[time_r][i].point.visible.valueOf());
                       entitypt[time_r][i].point.visible = true;
//                       console.log("VisiblePoints7 true entitypt[%d][%d].point.visible =%s",time_r,0,entitypt[time_r][0].point.visible.valueOf());
                   } // end for
//                   console.log("finishing for loop")
               } // end if length
           } // end if typeof
           if (typeof entitySph[time_r] !== "undefined") {
//               console.log("VisiblePoints false entitypt[%d].point.length=%d",time_r,entitypt[time_r].point.length);
                if (entitySph[time_r].length !== null) {
//                    visibilitypt[time_r] = true;
                   for (var i = 0; i < entitySph[time_r].length; i++) {
//                       console.log("Entering for loop with i=%d", i)
//                       console.log("VisibleSphere3 true entitySph[%d][%d].sphere.visible =%s",time_r,i,entitySph[time_r][i].sphere.visible.valueOf());
                       entitySph[time_r][i].sphere.visible = true;
//                       console.log("VisibleSphere4 true entitySph[%d][%d].sphere.visible =%s",time_r,i,entitySph[time_r][i].sphere.visible.valueOf());
//                       console.log("VisiblePoints7 true entitypt[%d][%d].point.visible =%s",time_r,0,entitypt[time_r][0].point.visible.valueOf());
                   } // end for
//                   console.log("finishing for loop")
               } // end if length
           } // end if typeof
           render();
       } // end VisibleLines




    function render() {
        renderer.render( scene, camera );
    }

    function animate(){
        if (cam_rotation == true){
            rotation_cam();
        }
        requestAnimationFrame(animate);
        controls.update();
        render();
    }


  $(function() {
    $( "#time-slider" ).slider({
      range: "min",
      min: min_tp,
      max: max_tp*scaletime,
//      value: Math.floor(time_tp/100)*100,
      value: time_tp,
      slide: function( event, ui ) { // slide the bar and change the value at #timepoint
        $( "#timepoint" ).val( ui.value/scaletime );
        $( "#time" ).val( ui.value*tscale );
//        last_t = time_t;
        last_tp = time_tp;
//        time_tp = Math.floor(ui.value/100)*100;
        time_tp = ui.value;
        last_t = last_tp;
        time_t = time_tp;
        VisibleLines();
      },
      stop: function(event, ui){ // when the slider stop, display a new dataset using the stop value
          last_t = ui.value;
//          last_t = Math.floor(ui.value/100)*100;
//          ssbd_url = base_url+"BDML/vertices/"+bdml_id+"/t/"+time_t+"/etype/";
//          removeObject();
//          line_error = SSBDviewDrawlines();
//          point_error = SSBDviewDrawpoints();
//          sphere_error = SSBDviewDrawspheres();
      } // end of stop
    }); // end .slider
    $( "#timepoint" ).val( $( "#time-slider" ).slider( "value") );
    $( "#tunit" ).val( tunit );
  }); //end of time-slider

  $(function(){
      $("#diccanvas").drawImage({
          source:"img/img-z000.jpg",
          width: 600,
          height: 600,
          fromCenter: false
      });
      img.onload = function() {
          var mFocalPlane = 30;
          canvas.drawImage(img, 0, mFocalPlane * 300, 300, 300, 0, 0, 300, 300);
  }
  }); // end of diccanvas

 }; // end of SSBDviewStart


</script>
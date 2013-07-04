$(function() {

    $.ajaxSetup({
        beforeSend: function() {
            $('#loader').show();
        },
        complete: function(){
            $('#loader').hide();
        },
        success: function() {}
    });

    getMapData();
    
});

function getMapData() {
    $.get("/admin/json/getmap", function(data) {
        buildMap(data);
    }, 'json');		
}


function buildMap(mapdata) {
    
    var dataLat;
    var dataLong;
    var zoomLevel;

    if(typeof(mapdata[0])!=='undefined') {
        dataLat = Number(mapdata[0]['latitude']) || 37.5408;
        dataLong = Number(mapdata[1]['longitude']) || 126.971269;
        zoomLevel = 13;
    } else { // default and zoomed out 
        dataLat = 37.5408;
        dataLong = 126.971269;
        zoomLevel = 1;
    }

    var map = L.map('admin-settings-map').setView([dataLat,dataLong],zoomLevel); 
    var marker = L.marker([dataLat,dataLong], {draggable:true}).addTo(map);
    
    L.tileLayer('http://{s}.tile.cloudmade.com/' 
                + MapConfig['apikeys']['cloudmade'] 
                + '/997/256/{z}/{x}/{y}.png', {
                    attribution: 'Map data &copy; <a href="http://openstreetmap.org">\
OpenStreetMap</a> contributors,\
<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, \
Imagery © <a href="http://cloudmade.com">CloudMade</a>',
                    maxZoom: 18
                }).addTo(map);

    marker.on('dragend' , function(evt) {
        saveLatLng(evt.target._latlng);
    });
    
}


function saveLatLng(latlng) {
    $.get("/admin/settings/savemap", { latitude: latlng.lat, longitude: latlng.lng } )
        .done(function() {
            $('#alert-success-info').show().delay('2000').fadeOut();
        });
}



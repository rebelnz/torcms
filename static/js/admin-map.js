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
	
	// console.log(mapdata[0]);
	var dataLat;
	var dataLong;

	if(typeof(mapdata[0])!=='undefined') {
		dataLat = Number(mapdata[0]['latitude']) || 37.5408;
		dataLong = Number(mapdata[1]['longitude']) || 126.971269;
	} else {
		dataLat = 37.5408;
		dataLong = 126.971269;
	}

	var map = L.map('admin-settings-map').setView([dataLat,dataLong],13); 
	L.tileLayer('http://{s}.tile.cloudmade.com/' 
				+ MapConfig['apikeys']['cloudmade'] 
				+ '/997/256/{z}/{x}/{y}.png', {
					attribution: 'Map data &copy; <a href="http://openstreetmap.org">\
					OpenStreetMap</a> contributors,\
						<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, \
					Imagery © <a href="http://cloudmade.com">CloudMade</a>',
					maxZoom: 18
				}).addTo(map);

	var marker = L.marker([dataLat,dataLong]).addTo(map);
    
    var popup = L.popup();
	
    function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent(e.latlng.toString())
			.openOn(map);

		map.removeLayer(marker);		

		makeBtn(e.latlng);

		$('#map-save-result').click(function() { 
			saveLatLng(e.latlng);
			return false; 
		});

    }
    map.on('click',onMapClick);
}


function makeBtn(latlng) {	
	var url = '/admin/settings/savemap?latitude=' + latlng.lat + '&longitude=' + latlng.lng;
	$('#map-save-result a').attr("href",url);
	url = "";
}


function saveLatLng(latlng) {
    $.get("/admin/settings/savemap", { latitude: latlng.lat, longitude: latlng.lng } )
		.done(function() {
			$('#alert-success-info').show().delay('4000').fadeOut();
		});

	return false;
}

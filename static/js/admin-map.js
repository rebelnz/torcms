$(function() {
	
	// get latlng ready to save to db - ajax
	// add params to button
	// console.log(MapConfig['apikeys']['cloudmade']);

	
	var map = L.map('admin-settings-map').setView([37.5408,126.971269],13); 
	L.tileLayer('http://{s}.tile.cloudmade.com/' + MapConfig['apikeys']['cloudmade'] + '/997/256/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    maxZoom: 18
	}).addTo(map);

	var popup = L.popup();
	
	function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent(e.latlng.toString())
			.openOn(map);
		
		saveLatLng(e.latlng);
	}

	
	map.on('click',onMapClick);
			

 });

// add params to button ready to be saved
function saveLatLng(latlng) {
	console.log(latlng);
	$.get("/admin/settings/savemap", { lat: latlng.lat, long: latlng.lng } );
}

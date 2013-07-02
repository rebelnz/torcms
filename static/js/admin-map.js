$(function() {
	
	// get latlng ready to save to db - ajax
	// add params to button
	// console.log(MapConfig['apikeys']['cloudmade']);

	
	var map = L.map('admin-settings-map').setView([37.5408,126.971269],13); 
	L.tileLayer('http://{s}.tile.cloudmade.com/' 
				+ MapConfig['apikeys']['cloudmade'] 
				+ '/997/256/{z}/{x}/{y}.png', {
					attribution: 'Map data &copy; <a href="http://openstreetmap.org">\
					OpenStreetMap</a> contributors,\
						<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, \
					Imagery © <a href="http://cloudmade.com">CloudMade</a>',
					maxZoom: 18
				}).addTo(map);
    
    var popup = L.popup();
	
    function onMapClick(e) {
		popup
			.setLatLng(e.latlng)
			.setContent(e.latlng.toString())
			.openOn(map);
		
		makeBtn(e.latlng);

		$('#map-save-result').click(function() { 
			saveLatLng(e.latlng);
			return false; } );
    }

    map.on('click',onMapClick);
	
});


function makeBtn(latlng) {
	$('#map-save-result a').remove();
	url = '/admin/settings/savemap?latitude=' + latlng.lat + '&longitude=' + latlng.lng;
	$('#map-save-result')
		.append('<a href="' + url + '" class="btn">save</a>');

}


// add params to button ready to be saved
function saveLatLng(latlng) {
    $.get("/admin/settings/savemap", { latitude: latlng.lat, longitude: latlng.lng } )
		.done(function() {
    		$('#map-save-result a, #alert-map-info').remove();
			$('#alert-success-info').show();
		});
	return false;
}

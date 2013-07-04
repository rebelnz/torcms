$(function() {
    // console.log(window.location);
    // console.log(window.navigator.userAgent);

    
    // var browserData = window.innerWidth;	
	
	var t = new Date();

    $.get("/json/tracker",{ innerW: window.innerWidth, date:t } )
		.done(function(data) {
			console.log(data);
		});		    
	

	// $.ajax({
	// 	type: 'GET',
	// 	url : '/json/tracker',
	// 	data : window.String,
	// 	dataType : 'json',
	// 	success : function( results ) {
	// 		console.log('success');
	// 	}
	// });

});

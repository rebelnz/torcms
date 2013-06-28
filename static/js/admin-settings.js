$(function() {
	$('#myTab a:last').tab('show'); 
	
	$("#admin-settings-nav li a").click(function() {

		$.get('/admin/settings/' + $(this).data('req'), function(data) {
			console.log($(this).data('req'));
		});


		
		
	});
		
 });

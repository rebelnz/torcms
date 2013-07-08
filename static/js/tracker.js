var TORCMS = TORCMS || {};

// namespace function
TORCMS.namespace = function(ns_string) {
	var parts = ns_string.split('.'),
		parent = TORCMS,
		i;
	
	// strip 'TORCMS'
	if (parts[0] === 'TORCMS') {
		parts = parts.slice(1);
	}
	
	for (i = 0; i < parts.length; i += 1) {
		// create property if not exists
		if ( typeof parent[parts[i]] === 'undefined' ) {
			parent[parts[i]] = {};
		}
		parent = parent[parts[i]];		
	}
	return parent;
};


TORCMS.namespace("TORCMS.postreq");
TORCMS.namespace("TORCMS.getcookie");

TORCMS.getcookie = function (name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
};



TORCMS.postreq = (function() {
	var t = new Date();			
	var xsrf = TORCMS.getcookie("_xsrf");

	return $.post("/json/tracker",{ innerW: window.innerWidth, 
									date:t,
									_xsrf: xsrf
								  })
		.done(function(data) {
			// console.log(data);
		});	
}());


(function initTracker() {	
	req = TORCMS.postreq;
	console.log(req);	
})();


// http://www.tornadoweb.org/en/stable/overview.html
// jQuery.postJSON = function(url, args, callback) {
//     args._xsrf = getCookie("_xsrf");
//     $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
//         success: function(response) {
//         callback(eval("(" + response + ")"));
//     }});
// };




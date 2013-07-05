// var ATRACKER = ATRACKER || {};

// ATRACKER.namespace = function(ns_string) {
// 	var parts = ns_string.split('.'),
// 		parent = ATRACKER,
// 		i;
	
// 	// strip 'ATRACKER'
// 	if (parts[0] === 'ATRACKER') {
// 		parts = parts.slice(1);
// 	}
	
// 	for (i = 0; i < parts.length; i += 1) {
// 		// create property if not exists
// 		if ( typeof parent[parts[i]] === 'undefined' ) {
// 			parent[parts[i]] = {};
// 		}
// 		parent = parent[parts[i]];		
// 	}
// 	return parent;
// };


// ATRACKER.namespace("fireGetReq");


// function getCookie(name) {
//     var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
//     return r ? r[1] : undefined;
// }

// // http://www.tornadoweb.org/en/stable/overview.html
// // jQuery.postJSON = function(url, args, callback) {
// //     args._xsrf = getCookie("_xsrf");
// //     $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
// //         success: function(response) {
// //         callback(eval("(" + response + ")"));
// //     }});
// // };

// (function () {
// 	var t = new Date();			
// 	var xsrf = getCookie("_xsrf");
// 	ATRACKER.fireGetReq = {
// 		getReq: function() {
// 			return $.post("/json/tracker",{ innerW: window.innerWidth, 
// 											date:t,
// 											_xsrf: xsrf
// 											// _xsrf: '62a952754043441f9ddb30ed6f7b1cde'
// 										  } )
// 				.done(function(data) {
// 					console.log(data);
// 				});		    			
// 		}
// 	};
// }());



// (function initTracker() {	
// 	ATRACKER.fireGetReq.getReq();
// })();

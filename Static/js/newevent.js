/*NewEvent.js
 *Designed by Jonathan Nungaray
 *@Jonatthu 21/03/2015*/
/*global $:false*/
/*global alert:false*/

//Main function where it'll be the magic with AJAX :')

var tipoo_url = window.location.pathname;

//Verifying that we are not in tracker ;)
if ( tipoo_url !== "/tracker" ) {

function doAjax(ddata) {
	'use strict';
	$.ajax({
		url: '/tracker',
		type: 'post',
		data: ddata,
		dataType: 'json'
	});
}

function data(object, select, eventt) {
	'use strict';
	var contenturl = object.attr('href'),
		siteurl = window.location.pathname,
		siteurl = siteurl.replace("/", ""),
		info = select,
		type = eventt,
		ddata = {
			site_url: siteurl,
			content_url: contenturl,			
			information: info,
			event: type
		};

	doAjax(ddata);
	//alert(siteurl + "\n" + contenturl + "\n" + info + "\n" + type);
}

//When the user clicks something
$(document).on('click', document, function (e) {
	'use strict';
	data($(this), '', 'click');
});

$(document).on('click', 'a', function (e) {
	'use strict';
	data($(this), '', 'clickvideo');
});

//I'm the BOSS
$(document).ready(function () {
	'use strict';

	$('.video, video, embed').hover(function () {
		data($(this), '', 'hover');
	},
		function () { //Nothing here ;C
		});

	$('input, textarea').focusout(function (e) {
		data($(this), '', 'focusout');
	});
	$('input, textarea').focusin(function (e) {
		data($(this), '', 'focusin');
	});

	$('body').mouseup(function (e) {
		var text = 0;
		if (window.getSelection) {
			text = window.getSelection().toString();
			if (text !== 0) {
				data($(this), text, 'select');
			}
		} else if (document.selection && document.selection.type !== "Control") {
			text = document.selection.createRange().text;
			if (text !== 0) {
				data($(this), text, 'select');
			}
		}
	});
});

}

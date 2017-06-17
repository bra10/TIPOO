
	jQuery(document).ready(function ($) {
		if (window.history && window.history.pushState) {
			window.history.pushState('forward', null, '');
			$(window).on('popstate', function () {
				window.location.href = document.referrer;
			});
		}
	});


$(document).on('click', '#bar', function () {
    "use strict";
    $('#navBar').animate({
        height: "300px"
    });
    $('body').animate({
        "margin-top": "300px"
    });
    $('#bar').css({
        display: 'none'
    });
    $('#barT').fadeIn().animate({
        borderSpacing: -90
    }, {
        step: function (now, fx) {
            $(this).css('transform', 'rotate(' + now + 'deg)');
        },
        duration: 'fast'
    }, 'linear');

});

$(document).on('click', '#barT', function () {
    "use strict";
    $('#navBar').animate({
        height: "60px"
    });
    $('body').animate({
        "margin-top": "0px"
    });
    $('#bar').fadeIn();
    $('#barT').fadeOut().animate({
        borderSpacing: 0
    }, {
        step: function (now, fx) {
            $(this).css('transform', 'rotate(' + now + 'deg)');
        },
        duration: 'fast'
    }, 'linear');;
});


/*
$(document).on('click', '#searchSection', function () {
    'use strict';
    $("#main").prepend('<div id="searchMain">hello</div>');
    $("#searchMain").css({
        background: "white"
    });
});
*/

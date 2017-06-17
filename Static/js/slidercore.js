/*
*Jslider by Jonathan Nungaray 2014 @Jonatthu Core
*Compresse Version 3 
*/  

!function(e,a){"function"==typeof define&&define.amd?define(["jquery"],a):a("object"==typeof exports?require("jquery"):e.jQuery||e.Zepto)}(this,function(e){"use strict";var a=function(a,n){function t(){L=m,0===m?(L=h,"fade"!==n.animation&&u.css("left",-L*g)):m===w-1&&(L=1,"fade"!==n.animation&&u.css("left",-g)),"fade"===n.animation&&v.eq(L).show(),n.showBullets&&a.next(".as-nav").find("a").removeClass("as-active").eq(L-1).addClass("as-active"),C=!1,n.afterChange.call(a[0])}function i(){C||1>=h||(C=!0,n.beforeChange.call(a[0]),"fade"===n.animation?v.css("z-index",1).fadeOut(n.speed).eq(m).css("z-index",2).fadeIn(n.speed,t):u.animate({left:-m*g},n.speed,n.easing,t),s())}function s(){clearTimeout(p),n.interval&&h>1&&(p=setTimeout(function(){n.reverse?f():l()},n.interval))}function o(){return L}function r(e){m=e,i()}function l(){m=L+1,i()}function c(){clearTimeout(p)}function d(){s()}function f(){m=L-1,i()}var u,p,v=a.children(),h=v.length,w=h,g=a.width(),m=0,L=0,C=!1,x={afterChange:function(){},afterSetup:function(){},animation:"slide",beforeChange:function(){},easing:"swing",interval:5e3,keyboard:!0,nextLabel:"Next slide",pauseOnHover:!0,prevLabel:"Previous slide",reverse:!1,showBullets:!0,showControls:!0,speed:400,startSlide:1,touch:!0};if(n=e.extend(x,n),h>1&&(v.eq(0).clone().addClass("clone").appendTo(a),v.eq(w-1).clone().addClass("clone").prependTo(a),n.startSlide<h&&(L=n.startSlide)),v=a.children(),w=v.length,v.wrapAll('<div class="as-slide-inner"></div>').css("width",g),u=a.css("overflow","hidden").find(".as-slide-inner"),"fade"===n.animation?(v.css({display:"none",left:0,position:"absolute",top:0}).eq(L).show(),u.css("width",g)):(v.css({"float":"left",position:"relative"}),u.css({left:-L*g,width:w*g})),u.css({"float":"left",position:"relative"}),n.showControls&&h>1&&(a.prepend('<a href="#" class="as-prev-arrow" title="LABEL">LABEL</a>'.replace(/LABEL/g,n.prevLabel)),a.append('<a href="#" class="as-next-arrow" title="LABEL">LABEL</a>'.replace(/LABEL/g,n.nextLabel)),a.on("click.as",".as-prev-arrow, .as-next-arrow",function(a){a.preventDefault(),C||(e(this).hasClass("as-prev-arrow")?f():l())})),n.showBullets&&h>1){var E,b,y='<div class="as-nav"></div>',S=e(y);for(E=1;h>=E;E++)b="",E===L&&(b=' class="as-active"'),S.append('<a href="#"'+b+">"+E+"</a>");S.on("click.as","a",function(a){var n=e(this).index();a.preventDefault(),e(this).hasClass("as-active")||C||(S.find("a").removeClass("as-active").eq(n).addClass("as-active"),r(n+1))}),a.after(S)}if(n.keyboard&&e(document).on("keydown.as",function(e){var a=e.keyCode;37!==a&&39!==a||1>=h||(37===a?f():l())}),n.pauseOnHover&&a.on("mouseenter",function(){c()}).on("mouseleave",function(){d()}),e(window).resize(function(){C||(g=a.width(),u.css("width",g),v.css("width",g),"fade"!==n.animation&&u.css({left:-L*g,width:w*g}))}),n.touch&&"ontouchstart"in window||navigator.msMaxTouchPoints>0||navigator.maxTouchPoints>0){var q,B;a.on("touchstart.as pointerdown.as MSPointerDown.as",function(e){q=e.timeStamp,B=e.originalEvent?e.originalEvent.pageX||e.originalEvent.touches[0].pageX:e.pageX||e.touches[0].pageX}).on("touchmove.as pointermove.as MSPointerMove.as",function(e){var n,t=0,i=e.timeStamp;n=e.originalEvent?e.originalEvent.pageX||e.originalEvent.touches[0].pageX:e.pageX||e.touches[0].pageX,0!==B&&(t=Math.abs(n-B)),0!==q&&1e3>i-q&&t>10&&(e.preventDefault(),B>n?l():n>B&&f(),q=0,B=0,a.trigger("touchend.as"))}).on("touchend.as pointerup.as MSPointerUp.as",function(){q=0,B=0})}return s(),n.afterSetup.call(a[0]),{currentSlide:o,goTo:r,next:l,pause:c,play:d,prev:f}};e.fn.Jslider=function(n){return this.each(function(){var t,i=e(this);return i.data("Jslider")?i.data("Jslider"):(t=new a(i,n),void i.data("Jslider",t))})}});
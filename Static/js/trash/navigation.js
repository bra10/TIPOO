/*
 * Author: Raul I. Navarro Almanza
 * 
 * */
navigation = function (slide_id,nav_menu,menu_id,selected_opt,anchor_id,time){
	var hlist=[];
	$(function(){
		$(slide_id).each(function(index){
			hlist.push($(this).offset().top+$(this).outerHeight(true));
		});	
	});
	
	$(document).on('click',anchor_id, function(e) {  
		e.preventDefault();
	    var $link = $(this);  
	    var anchor  = $link.attr('href');  
	    $('html, body').stop().animate({  
	        scrollTop: $(anchor).offset().top 
	    }, time);  
	});  
	
	var currentSlide=0;
	
	$(window).scroll(function(){
		var actualOffset=$(window).scrollTop();
		if(actualOffset>=53){
			$(menu_id).addClass('fixed');
		}
		else{
			$(menu_id).removeClass('fixed');
		}
		
		
		$.each(hlist,function(index,value){
			if(actualOffset<value){
				currentSlide=index;
				return false;
			}
		});
		$(nav_menu).each(function(index){
			var obj=$(this);
			if(index==currentSlide){
				$.each(selected_opt,function(key,value){
					$(key,obj).addClass(value);
				});
			}
			else{
				$.each(selected_opt,function(key,value){
					$(key,obj).removeClass(value);
				});
			}
		});
		
	});
	
};
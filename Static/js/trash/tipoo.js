/*hide=function(){
	$("#signin").fadeOut("slow");
	$("#overlay").fadeOut();
}
$(document).ready(function(){
	
	User Parameters
	var selected={
			".figure":"selected-nav"
	};
	End User Parameters
	
	var hlist=[]
	$(function(){
		$(".slide").each(function(index){
			hlist.push($(this).offset().top+$(this).outerHeight(true));
		});	
		//alert(hlist);
	})
	
	
	$("#linksignin").click(function(){
		$("#signin").fadeIn("slow");
		$("#overlay").fadeIn();
	});
	
	$("#close").click(hide);
	$("#overlay").click(hide);
	
	
	
	$(document).on('click','.text-option', function(e) {  
		e.preventDefault();
	    var $link = $(this);  
	    var anchor  = $link.attr('href');  
	    $('html, body').stop().animate({  
	        scrollTop: $(anchor).offset().top-53  
	    }, 1000);  
	});  
	
	var currentSlide=0;
	
	$(window).scroll(function(){
		var actualOffset=$(window).scrollTop();
		if(actualOffset>=53){
			$("#leftmenu").addClass('fixed');
		}
		else{
			$("#leftmenu").removeClass('fixed');
		}
		
		
		$.each(hlist,function(index,value){
			if(actualOffset<value){
				currentSlide=index;
				return false;
			}
		});
		$(".section").each(function(index){
			var obj=$(this);
			if(index==currentSlide){
				$.each(selected,function(key,value){
					$(key,obj).addClass(value);
				});
			}
			else{
				$.each(selected,function(key,value){
					$(key,obj).removeClass(value);
				});
			}
		});
		
	});
});*/
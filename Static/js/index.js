$(document).ready(function(){
	$("#demo a").click(function(event) {
		event.preventDefault();
		$("#iniciosesion input[name='email']").attr('value',"test@demo.com");
		$("#iniciosesion input[name='pwd']").attr('value',"demo");
		});
	
});

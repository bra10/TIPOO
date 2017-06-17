hide=function(){
	$("#signin").fadeOut("slow");
	$("#overlay").fadeOut();
}
$(document).ready(function(){
	
	$("#linksignin").click(function(){
		$("#signin").fadeIn("slow");
		$("#overlay").fadeIn();
	});
	
	$("#close").click(hide);
	$("#overlay").click(hide);
});
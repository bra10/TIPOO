$(document).ready(function() {

	var subject="";
		/*Menu*/
	$("#chapters a").click(function(event) {
		event.preventDefault();
		var classes = $(this).attr('class');
		if (!( typeof classes === "undefined")) {
			if (!(classes.indexOf('unavailable') >= 0)) {
			
				var sbj = $(this).attr('href');
				subject=sbj;
				var post=$.post("/home-content", {
								subject : sbj});
				post.done(function( data ) {
			    var content = $( data ).find( "#subject-title" ).html();
			    $( "#subject-title" ).html(content);
			    console.log(content);
			    content = $( data ).find( "#level-opt" ).html();
			    $("#level-opt").html(content);
			    console.log(content);
			    content = $( data ).find( "#style-opt" ).html();
			    $("#style-opt").html(content);
			    console.log(content);
			    content = $( data ).find( "#button-opt" ).html();
			    $("#button-opt").html(content);
			    console.log(content);
			    content = $( data ).find( "#iframe" ).html();
			    $("#iframe").html(content);
			    console.log(content);
			  });	
			} 
		} else {
			var sbj = $(this).attr('href');
			subject=sbj;
			var post=$.post("/home-content", {
								subject : sbj});
				post.done(function( data ) {
			    var content = $( data ).find( "#subject-title" ).html();
			    $( "#subject-title" ).html(content);
			    console.log(content);
			    content = $( data ).find( "#level-opt" ).html();
			    $("#level-opt").html(content);
			    console.log(content);
			    content = $( data ).find( "#style-opt" ).html();
			    $("#style-opt").html(content);
			    console.log(content);
			    content = $( data ).find( "#button-opt" ).html();
			    $("#button-opt").html(content);
			    console.log(content);
			    content = $( data ).find( "#iframe" ).html();
			    $("#iframe").html(content);
			    console.log(content);
			  });
		}
	});
	
	$(document).delegate("#menu-opt input[type='radio']","change",function() {
			var classes = $(this).attr('class');
			if ( typeof classes === "undefined"){
				var sbj = subject;
				var style_var= $("#menu-opt input[id*='radio-style']:checked").attr('value');
				var level_var= $("#menu-opt input[id*='radio-level']:checked").attr('value');
					input=true;
					var post_radio=$.post("/home-content", {
									select:input,
									subject :sbj,
									style:style_var,
									level:level_var
									}
									);
					post_radio.done(function( data ) {

					if(data!="FAILURE"){
						$( "#iframe" ).html(data);	
						console.log("SUCCESS");
					}
					console.log(data);
				  	});
				
				
			}
		});
}); 
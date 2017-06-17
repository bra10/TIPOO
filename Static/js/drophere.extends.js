/*Drophere.extension.js
*Designed by Jonathan Nungaray
*@Jonatthu 21/03/2015
*/

$("#sessionForm").dropzone({		
	acceptedFiles: ".webm,.mp4,.wmv,.mkv,.ogg",
	uploadMultiple: false,
	clickable: "#infoVideo",
	maxFiles: 1,
	maxFilesize: 5000,
	previewsContainer:  "#infoVideo",
	dictDefaultMessage: "<i class=\"fa fa-info-circle\"></i> Solo videos con extensión: webm, mp4, wmv, mkv, ogg.",
	init: function() {
    	this.on("addedfile", function(file) {
			$('#text, .dz-message').fadeOut(300);
		});

		/* The best choice that you have TIPOO uncomment this code
		this.on("complete", function(file) {
			setTimeout(function() {
			  $('#edit a button').trigger('click');
			}, 600);
		});
		*/

		//Lets put some security settings for this upload :p
		this.on("error", function(file) {
			setTimeout(function() {
			  alert("Ha habido un error con la extensión o en el servidor.");
			  setTimeout(function() {
			  	location.reload();
			  }, 1000);
			}, 600);
		});
  	}

});


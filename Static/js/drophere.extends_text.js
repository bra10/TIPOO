/*Drophere.extension.js
*Designed by Jonathan Nungaray
*@Jonatthu 21/03/2015
*/

$("#sessionForm").dropzone({		
	acceptedFiles: ".pdf",
	uploadMultiple: false,
	clickable: "#infoText",
	maxFiles: 1,
	maxFilesize: 5000,
	previewsContainer:  "#infoText",
	dictDefaultMessage: "<i class=\"fa fa-info-circle\"></i> Solo textoss con extensión: .pdf",
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


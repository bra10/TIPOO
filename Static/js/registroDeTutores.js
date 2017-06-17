/*

	registroDeTutores.js
	Ver. 1
	por Ian Alfonso Ruiz Naranjo
	@Ian_A_Ruiz_N
	/ian.a.ruiz.n
	Primavera, 2015

*/
$(document).on('click', '.closemodal, .bg', function(){
	$(".msgmodal, .bg").fadeOut();
});

$(document).ready(function () {
	var success = $('.msgmodal').attr('id');
	if ( success === "success") {
		setTimeout(function() {
			window.location="/";
		}, 3000);
	}
});
$(document).ready(function(){
	$("#campoNombre").val("Ingrese su nombre");
	$("#campoCorreo").val("Ingrese su correo");
	$("#campoContrasena").val("Ingrese su contrasena");

	/* Comportamiento del Campo Nombre */

	$("#campoNombre").focus(function(){
		$("#avisoNombre").html("");
		valorDelCampo = ($(this).val()).trim();
		if(valorDelCampo == "" || valorDelCampo == "Ingrese su nombre"){
			$(this).val("");
		}
	});
	$("#campoNombre").focusout(function(){
		valorDelCampo = ($(this).val()).trim();
		if(valorDelCampo == ""){
			$(this).val("Ingrese su nombre");
		}
	});

	/* Comportamiento del Campo Correo */

	$("#campoCorreo").focus(function(){
		$("#avisoCorreo").html("");
		valorDelCampo = ($(this).val()).trim();
		if(valorDelCampo == "" || valorDelCampo == "Ingrese su correo"){
			$(this).val("");
		}
	});
	$("#campoCorreo").focusout(function(){
		valorDelCampo = ($(this).val()).trim();
		if(valorDelCampo == ""){
			$(this).val("Ingrese su correo");
		}
	});

	/* Comportamiento del Campo Contrasena */

	$("#campoContrasena").focus(function(){
		$("#avisoContrasena").html("");
		valorDelCampo = ($(this).val()).trim();
		if(valorDelCampo == "" || valorDelCampo == "Ingrese su contrasena"){
			$(this).val("");
		}
	});
	$("#campoContrasena").focusout(function(){
		valorDelCampo = ($(this).val()).trim();
		if(valorDelCampo == ""){
			$(this).val("Ingrese su contrasena");
		}
	});

	/* Comportamiento del Selector de Facultades */

	$("#contenedorDeSelectorDeFacultades").hide();
	$("#selectorDeFacultades").empty();

	function desplegaLosDatos(){
		var seleccion = ($("#selectorDeUniversidades").val()).trim();

		if(seleccion == "Seleccione una universidad"){
			$("#selectorDeFacultades").empty();
			$("#contenedorDeSelectorDeFacultades").hide();
		}
		else if(seleccion == "UABC Universidad Autonoma de Baja California"){
			$("#selectorDeFacultades").empty();
			$("#selectorDeFacultades").html(
				"<option>FCQI Facultad de Ciencias Quimicas e Ingenieria</option>" +
				"<option>CITEC Escuela de Ciencias de la Ingenieria y Tecnologia</option>"
			);
			$("#contenedorDeSelectorDeFacultades").show();
		}
		else if(seleccion == "TEC Instituto Tecnologico de Tijuana"){
			$("#selectorDeFacultades").empty();
			$("#selectorDeFacultades").html(
				"<option>F1</option>" +
				"<option>F2</option>"
			);
			$("#contenedorDeSelectorDeFacultades").show();
		}
		else if(seleccion == "UNAM Universidad Nacional Autonoma de Mexico"){
			$("#selectorDeFacultades").empty();
			$("#selectorDeFacultades").html(
				"<option>Aragon</option>" +
				"<option>C.U. Ciudad Universitaria</option>"
			);
			$("#contenedorDeSelectorDeFacultades").show();
		}
			else if(seleccion =="Independiente"){
			$("#selectorDeFacultades").empty();
			$("#selectorDeFacultades").html(
				"<option>F1</option>" +
				"<option>F2</option>"
			);
			$("#contenedorDeSelectorDeFacultades").show();
		}
	}
	$("#selectorDeUniversidades").change(desplegaLosDatos);
	$("#avisoUniversidad").html("");
});

function validacion(){

	$("#avisoNombre").html("");

	var resultadoDeVerificacionesNombre;
	var resultadoDeVerificacionesCorreo;
	var resultadoDeVerificacionesContrasena;
	var resultadoDeVerificacionesSelector;
	var resultadoDeVerificacionesFinal;

	var valorNombre =($("#campoNombre").val()).trim();
	var valorCorreo =($("#campoCorreo").val()).trim();
	var valorContrasena =($("#campoContrasena").val()).trim();

	/* Analisis del Nombre */

	if(valorNombre == "Ingrese su nombre"){
		$("#avisoNombre").html("Escriba su nombre");
		resultadoDeVerificacionesNombre = false;
	}
	else{
		var reg = /^[\w ]+$/;
		resultadoReg = reg.test(valorNombre);
		if(resultadoReg == false){
			$("#avisoNombre").html("Solo use letras, numeros y espacios");
			resultadoDeVerificacionesNombre = false;
		}
		else{
			resultadoDeVerificacionesNombre = true;
			var vectorNombre = valorNombre.split("");
			if(vectorNombre.length < 6 || vectorNombre.length > 12){
				$("#avisoNombre").html("El nombre debe de tener entre 6 y 12 caracteres");
				resultadoDeVerificacionesNombre = false;
			}
			else{
				resultadoDeVerificacionesNombre = true;
			}
		}	
	}

	/* Analisis del Correo */

	if(valorCorreo == "Ingrese su correo"){
		resultadoDeVerificacionesCorreo = false;
		$("#avisoCorreo").html("Escriba su correo");
	}
	else{
		resultadoDeVerificacionesCorreo = true;
		reg = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
		resultadoReg = reg.test(valorCorreo);
		if(resultadoReg == false){
			$("#avisoCorreo").html("Escriba correctamente su correo");
			resultadoDeVerificacionesCorreo = false;
		}
		else
			resultadoDeVerificacionesCorreo = true;
	}

	/*Analisis de la Contraseña */

	if(valorContrasena == "Ingrese su contrasena"){
		$("#avisoContrasena").html("Escriba su contrasena");
		resultadoDeVerificacionesContrasena = false;
	}
	else{
		resultadoDeVerificacionesContrasena = true;
		vectorContrasena = valorContrasena.split("");
		if(vectorContrasena.length < 6 || vectorContrasena.length > 12){
			resultadoDeVerificacionesContrasena = false;
			$("#avisoContrasena").html("La contrasena debe de medir entre 6 y 12 caracteres");
		}
		else{
			resultadoDeVerificacionesContrasena = true;
		}
	}

	/* Analisis de Selector de Universidad */

	valorDelSelectorDeUniversidades = $("#selectorDeUniversidades").val();
	if(valorDelSelectorDeUniversidades == "Seleccione una universidad"){
		$("#avisoUniversidad").html("Seleccione una universidad");
		resultadoDeVerificacionesSelector = false;
	}
	else{
		resultadoDeVerificacionesSelector = true;
		$("#avisoUniversidad").html("");
	}

	if(resultadoDeVerificacionesSelector == true && resultadoDeVerificacionesContrasena == true && resultadoDeVerificacionesCorreo == true && resultadoDeVerificacionesNombre == true){
		resultadoDeVerificacionesFinal = true;
	}
	else{
		resultadoDeVerificacionesFinal = false;
	}

	return resultadoDeVerificacionesFinal;
}
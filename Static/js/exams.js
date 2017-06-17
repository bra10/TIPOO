var divNum = 0;
function removeElement() 
{
	var d = document.getElementById('myDiv');
	console.log(d);
	if(document.getElementById('theValue').value > 0)
	{
		d.removeChild(d.lastChild);
		document.getElementById('theValue').value = parseInt(document.getElementById('theValue').value) -1;
	}
}	
	
function addElement() 
{
	var ni = document.getElementById('myDiv');
	var numi = document.getElementById('theValue');
	var num = (document.getElementById('theValue').value -1)+ 2;
	numi.value = num;
	pregunta = num+1;
	divNum = parseInt(num);
	var newdiv = document.createElement('div');
	var divIdName = 'my'+num+'Div';
	newdiv.setAttribute('id',divIdName);
	newdiv.innerHTML = 
'			<div class="row">'+
'				<div class="large-10 columns">'+
'					<label><strong>'+pregunta+'.</strong> Ingresar pregunta <input name="q['+num+']" type="text" placeholder="Redactar pregunta aqu&iacute;..." required /></label>'+
'					<small class="error">Ingrese una pregunta v&aacute;lida.</small>'+
'				</div>'+
'				<div class="large-2 columns">'+
'					<label>Puntos <input name="v['+num+']" type="text" placeholder="0..10" maxlength="2" required pattern="integer" /></label>'+
'					<small class="error">Ingrese los puntos.</small>'+					
'				</div>'+
'			</div>'+
'			<div class="row">'+
'				<div class="large-3 columns">'+
'					<div class="row collapse">'+
'						<label>Opci&oacute;n 1</label>'+
'						<div class="small-10 columns">'+
'							<input name="a['+num+']" placeholder="Primera opci&oacute;n" type="text" required>'+
'						</div>'+
'						<div class="small-2 columns">'+
'							<span class="postfix" title="Respuesta correcta"><input name="r['+num+']" value="1" type="checkbox"></span>'+
'						</div>'+
'					</div>'+
'				</div>'+
'				<div class="large-3 columns">'+
'					<div class="row collapse">'+
'						<label>Opci&oacute;n 2</label>'+
'						<div class="small-10 columns">'+
'							<input name="a['+num+']" placeholder="Segunda opci&oacute;n" type="text" required>'+
'						</div>'+
'						<div class="small-2 columns">'+
'							<span class="postfix" title="Respuesta correcta"><input name="r['+num+']" value="2" type="checkbox"></span>'+
'						</div>'+
'					</div>'+
'				</div>'+
'				<div class="large-3 columns">'+
'					<div class="row collapse">'+
'						<label>Opci&oacute;n 3</label>'+
'						<div class="small-10 columns">'+
'							<input name="a['+num+']" placeholder="Tercera opci&oacute;n" type="text" required>'+
'						</div>'+
'						<div class="small-2 columns">'+
'							<span class="postfix" title="Respuesta correcta"><input name="r['+num+']" value="3" type="checkbox"></span>'+
'						</div>'+
'					</div>'+
'				</div>'+
'				<div class="large-3 columns">'+
'					<div class="row collapse">'+
'						<label>Opci&oacute;n 4</label>'+
'						<div class="small-10 columns">'+
'							<input name="a['+num+']" placeholder="Cuarta opci&oacute;n" type="text" required>'+
'						</div>'+
'						<div class="small-2 columns">'+
'							<span class="postfix" title="Respuesta correcta"><input name="r['+num+']" value="4" type="checkbox"></span>'+
'						</div>'+
'					</div>'+
'				</div>'+
'			</div>';
	ni.appendChild(newdiv);
}
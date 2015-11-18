function getTemplate(path){
	var xmlhttp;
	var resource;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
			resource = xmlhttp.responseText;
		}
	}
	xmlhttp.open("GET", path, false);
	xmlhttp.send();
	return resource;
};

function printTemplate(locacion, html){
	document.getElementById(locacion).innerHTML = html;
};

function getRubros(){
	var xmlhttp;
	var txt,x,xx,i;
	var rubros;

	xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			rubros =  JSON.parse(xmlhttp.responseText);			
		}
		
	}
	xmlhttp.open("GET", 'http://localhost:8000/rubros/?format=json', false);
	xmlhttp.send();

	return rubros;
}

function getCiudades(){
	var xmlhttp;
	var txt,x,xx,i;
	var ciudades;

	xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			ciudades =  JSON.parse(xmlhttp.responseText);			
		}
		
	}
	xmlhttp.open("GET", 'http://localhost:8000/ciudades/?format=json', false);
	xmlhttp.send();

	return ciudades;
}

function fillComboRubros(){
   var rubros = getRubros();
   var j;

    for (j = 0; j < rubros.length; j++) {
        var x = document.getElementById("cmbRubro");
        var option = document.createElement("option");
        option.text = rubros[j].nombre;
        option.value = rubros[j].id;
        x.add(option);
    }
}

function fillComboCiudades(){
   var ciudades = getCiudades();
   var j;

    for (j = 0; j < ciudades.length; j++) {
        var x = document.getElementById("cmbCiudad");
        var option = document.createElement("option");
        option.text = ciudades[j].nombre;
        option.value = ciudades[j].id;
        x.add(option);
    }
}

function EstablecimientosView(parametros){
	
	getObjetoModel("establecimientos", parametros, EstablecimientosTemplate);
};

function OnClickBtnCalificar(idEstablecimiento){
	 
	document.getElementById('btnAceptarCalificar').setAttribute('onclick', 'OnClickAceptarCalificar(' + idEstablecimiento + ')');
	document.getElementById('txtComentario').value = '';
}

function EstablecimientosTemplate(establecimientos){
	
	var html, panel, nombre_elem, direccion_elem;
	var promedio_elem, cantCalificaciones_elem;
	var nombre, direccion, promedio, cantCalificaciones, i, j;
	
	document.getElementById('content').innerHTML = '';
	var html = getTemplate("templates/establecimiento.html");
	
	for (i = 0; i < establecimientos.length; i++) {
		establecimiento = establecimientos[i];
		
		nombre 			= establecimiento.nombre;
		
		direccion 		= establecimiento.direccion;
		
		direccion += ', ';

		direccion += establecimiento.ciudad.nombre;

		direccion += '.';
		
		document.getElementById('content').innerHTML += html;
		document.getElementById('panel').id = establecimiento.id;
		
		panel = document.getElementById(establecimiento.id);
				
		labels = panel.getElementsByTagName('label');
		
		for (j = 0; j < labels.length; j++) {
			if (labels.item(j).id == 'nombreEstablecimiento')
				{
					nombre_elem = labels.item(j);
				}
				
			if (labels.item(j).id == 'direccionEstablecimiento')
				{
					direccion_elem = labels.item(j);
				}
				
			if (labels.item(j).id == 'promedioEstablecimiento')
				{
					promedio_elem = labels.item(j);
				}

			if (labels.item(j).id == 'cantCalifEstablecimiento')
				{
					cantCalificaciones_elem = labels.item(j);
				}		
		}

		nombre_elem.textContent = nombre;
		direccion_elem.textContent = direccion;
		
		var buttons = panel.getElementsByTagName('button');
		
		for (j = 0; j < buttons.length; j++) {
		
			if (buttons.item(j).id == 'btnCalificar'){
			
				buttons.item(j).setAttribute('onclick', 'OnClickBtnCalificar(' + establecimiento.id + ')');
			}
			if (buttons.item(j).id == 'btnDetalle'){

				buttons.item(j).setAttribute('onclick', 'OnClickBtnDetalle(' + establecimiento.id + ')');
			}
		}
	}
		
	document.getElementsByTagName('title')[0].text = "Metele Onda - Listado de establecimientos";
};

function OnClickBtnDetalle(idEstablecimiento){



	var parametros = [];

	parametros.push("id=" + idEstablecimiento);

	getObjetoModel("establecimientos", parametros, EstablecimientoDetalleTemplate);

}

function EstablecimientoDetalleTemplate(establecimientos){
	
   	document.getElementById('bodyPopUpDetalleEstablecimiento').innerHTML = '';
	var html = getTemplate("templates/establecimientoDetalle.html");
	document.getElementById('bodyPopUpDetalleEstablecimiento').innerHTML = html;

    fillComboRubros();
    fillComboCiudades();

	var establecimiento = establecimientos[0];

	var inputs = document.getElementById('bodyPopUpDetalleEstablecimiento').getElementsByTagName('input');

	for (j = 0; j < inputs.length; j++) {
		if (inputs.item(j).id == 'txtNombreEstablecimiento')
			{
				inputs.item(j).value = establecimiento.nombre;
			}
			
		if (inputs.item(j).id == 'txtDireccionEstablecimiento')
			{
				inputs.item(j).value = establecimiento.direccion;
			}	
	}

	var selects = document.getElementById('bodyPopUpDetalleEstablecimiento').getElementsByTagName('select');

	for (j = 0; j < selects.length; j++) {
		if (selects.item(j).id == 'cmbCiudad')
			{
				selects.item(j).value = establecimiento.ciudad.id;
			}
			
		if (selects.item(j).id == 'cmbRubro')
			{
				selects.item(j).value = establecimiento.rubro.id;
			}	
	}

}

function agregarEstablecimiento(establecimiento){
	var xmlhttp;
	var txt,x,xx,i;
	xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			alert(xmlhttp.responseText);
		}
		
	}

	xmlhttp.open("POST", 'http://localhost:8000/establecimientos/', true);

	xmlhttp.setRequestHeader("Content-type" ,"application/json");

	xmlhttp.send(JSON.stringify(establecimiento));
}

function calificarEstablecimiento(idEstablecimiento, puntaje, comentario){
	var xmlhttp;
	var txt,x,xx,i;
	
	var calificacion = {};
	
	calificacion.puntaje = puntaje;
	calificacion.comentario = comentario;
	calificacion.establecimiento = idEstablecimiento;
	calificacion.usuario = 1;
	
	xmlhttp=new XMLHttpRequest();
	
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			alert(xmlhttp.responseText);
		}
		
	}

	xmlhttp.open("POST", 'http://localhost:8000/calificaciones/', true);

	xmlhttp.setRequestHeader("Content-type" ,"application/json");

	xmlhttp.send(JSON.stringify(calificacion));
}

function EstadisticasView(parametros){

	getObjetoModel("diezMejores", parametros, EstadisticasTemplate);

}

function EstadisticasTemplate(estadisticas){

	var html, panel, nombre_elem, promedio_elem;
	var promedio_elem, cantCalificaciones_elem;
	var nombre, direccion, promedio, cantCalificaciones, i, j;
	
	document.getElementById('diezMejores').innerHTML = '';
	var html = getTemplate("templates/listadoEstadisticaEstablecimientos.html");
	var parser = new DOMParser()
  	var listado = parser.parseFromString(html, "text/xml");

	var table = document.getElementById('diezMejores');
	table.insertRow(0).innerHTML = "<th>Prom.Puntaje</th><th>Establecimiento</th>";

	for (i = 0; i < estadisticas.length; i++) {
	
		var e  = getEstablecimiento(estadisticas[i].establecimiento_id);

		e[0].promedio_puntaje = estadisticas[i].promedio_puntaje;
				
		var establecimiento = e[0];

		labels = listado.getElementsByTagName('label');
		
		for (j = 0; j < labels.length; j++) {
			if (labels.item(j).id == 'nombreEstablecimiento')
				{
					nombre_elem = labels.item(j);
				}
				
			if (labels.item(j).id == 'promedioEstablecimiento')
				{
					promedio_elem = labels.item(j);
				}
		}

		nombre_elem.textContent =  establecimiento.nombre;
		promedio_elem.textContent =  establecimiento.promedio_puntaje;

		var buttons = listado.getElementsByTagName('button');
		
		for (j = 0; j < buttons.length; j++) {
		
			if (buttons.item(j).id == 'btnDetalle'){

				buttons.item(j).setAttribute('onclick', 'OnClickBtnDetalle(' + establecimiento.id + ')');
			}
		}


		var row = table.insertRow(i + 1);
		row.innerHTML = listado.documentElement.innerHTML;
		row.style.borderBottom = "thick dotted #CCC";
		
	}
}
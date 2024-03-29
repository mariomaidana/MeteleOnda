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

function EstablecimientosView(parametros){
	
	getObjetoModel("establecimientos", parametros, EstablecimientosTemplate);
};

  	function OnClickBtnCalificar(idEstablecimiento){
  			 document.getElementById('idEstablecimiento').innerHTML = idEstablecimiento;
			 
			 document.getElementById('btnAceptarCalificar').setAttribute('onclick', 'OnClickAceptarCalificar(' + idEstablecimiento + ')');
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
		}
	}
		
	document.getElementsByTagName('title')[0].text = "Metele Onda - Listado de establecimientos";
};

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
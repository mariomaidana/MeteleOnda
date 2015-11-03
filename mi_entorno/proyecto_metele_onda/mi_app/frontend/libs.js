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

function EstablecimientosView(){
	
	getObjetoModel("establecimientos", EstablecimientosTemplate);
};

function EstablecimientosTemplate(establecimientos){
	
	var html, panel, panel_content, nombre_elem, direccion_elem, rubro_elem;
	var promedio_elem, total_elem, det_boton_elem, calif_ver_elem, calif_alta_elem;
	var nombre, direccion, i, j, ver_est;
	
	document.getElementById('content').innerHTML = '';
	var html = getTemplate("templates/establecimiento.html");
	
	for (i = 0; i < establecimientos.length; i++) {
		establecimiento = establecimientos[i];
		
		nombre 			= establecimiento.nombre;
		direccion 		= establecimiento.direccion;
		direccion += ', ';
		direccion += establecimiento.ciudad;

		direccion += '.';
		
		document.getElementById('content').innerHTML += html;
		document.getElementById('panel').id = establecimiento.url;
		
		panel = document.getElementById(establecimiento.url);
		
		nombre_elem = panel.getElementsByTagName('nombreEstablecimiento').item(0);

		nombre_elem.textContent 	= nombre;
	}
		
	document.getElementsByTagName('title')[0].text = "Metele Onda - Listado de establecimientos";
};
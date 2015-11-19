// JavaScript Document

function getObjetoModel(objeto, parametros, funcion){
	var xmlhttp, resp, i;

	xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange = function(){
		if (xmlhttp.readyState == 4 && xmlhttp.status==200){
			resp = JSON.parse(xmlhttp.responseText);
			funcion(resp);
		}
	}
	var url = "http://localhost:8000/" + objeto + "/";

	if (parametros.length > 0) {
		url += "?";
	}

	for (var i = 0; i < parametros.length; i++) {
		url += parametros[i]
	};

	xmlhttp.open("GET", url, true);
	xmlhttp.send();
};

function getEstablecimiento(idEstablecimiento){
	var xmlhttp, establecimiento;

	xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange = function(){
		if (xmlhttp.readyState == 4 && xmlhttp.status==200){
			establecimiento = JSON.parse(xmlhttp.responseText);
		}
	}
	var url = "http://localhost:8000/establecimientos/?id=" + idEstablecimiento;

	xmlhttp.open("GET", url, false);
	xmlhttp.send();

	return establecimiento;
};
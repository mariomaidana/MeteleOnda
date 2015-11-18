// JavaScript Document

function getObjetoModel(objeto, parametros, funcion){
	var xmlhttp, resp, i;

	xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange = function(){
		if (xmlhttp.readyState == 4 && xmlhttp.status==200){
			resp = JSON.parse(xmlhttp.responseText);
			funcion(resp)
		}
	}
	var url = "http://localhost:8000/" + objeto ;//+ "/?format=json";

	for (var i = 0; i < parametros.length; i++) {
		url += parametros[i]
	};

	xmlhttp.open("GET", url, true);
	xmlhttp.send();
};
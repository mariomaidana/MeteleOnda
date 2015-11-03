// JavaScript Document

function getObjetoModel(objeto, funcion){
	var xmlhttp, resp;
	xmlhttp = new XMLHttpRequest();
	xmlhttp.onreadystatechange = function(){
		if (xmlhttp.readyState == 4 && xmlhttp.status==200){
			resp = JSON.parse(xmlhttp.responseText);
			funcion(resp)
		}
	}
	var url = "http://localhost:8000/" + objeto + "/?format=json";

	xmlhttp.open("GET", url, true);
	xmlhttp.send();
};
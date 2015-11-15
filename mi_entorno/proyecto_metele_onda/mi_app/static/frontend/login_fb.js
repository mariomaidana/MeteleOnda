

function validarUsuario(usuario){
	var xmlhttp;
	var txt,x,xx,i;
	xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			console.log(xmlhttp);
			alert(xmlhttp.responseText);
		}
		
	}

	xmlhttp.open("POST", 'http://localhost:8000/usuarios/', true);

	xmlhttp.setRequestHeader("Content-type" ,"application/json");

	xmlhttp.send(JSON.stringify(usuario));
}


function datosUsuario(response){

	var usuario = {};
	usuario.nombre = response.name;
	usuario.fb_id = response.id;
	usuario.tw_id = response.id;
	usuario.google_id = response.id;

	
	validarUsuario(usuario);
}

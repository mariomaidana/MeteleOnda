
// Cargamos la API
(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/es_ES/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
  
// Configuramos la API
window.fbAsyncInit = function() {
  FB.init({
    appId      : '141050139584935', //Incluye aquí tu clave pública
	cookie	   : true,
    status     : true,
    xfbml      : true,
    version    : 'v2.1'
  });
}

//Redirecciones para después de iniciar sesión o salir de la aplicación
var url_after_login = "http://localhost:8000/static/frontend/main.html";
var url_after_logout = "http://localhost:8000/static/frontend/templates/login.html";
  
/* Función para el botón de iniciar sesión con Facebook */
function FBBtnLogin(){
	FB.login(function(response) {
		/* Si el usuario ha iniciado sesión correctamente cargamos la página login.html nuevamente para 
		   para que el usuario sea redireccionado a la página main.html */
		if (response.authResponse) {
			window.location.reload();
			}	
		 }, 
		 {
		 /* Solicitamos poder acceder a estos permisos del perfil del usuario */
		 
		 scope: 'public_profile,email'
	}); 
}

/* Función para el botón de cierre de sesión en facebook, 
   El usuario sale de nuestra aplicación */
function FBBtnLogout(){
    FB.logout(function(response) {
	/* Una vez cerrada la sesión cargamos nuevamente la página para redireccionar al usuario 
	a la página login.html */
	window.location.reload();
	}); 
}
 
 /*
 Función para la página login.html, esta función comprueba el estado del usuario, si el 
 usuario está conectado es redirigido a la página index.html, de lo contrario se le solicitará 
 que inicie sesión con su cuenta de Facebook
 */
 function FBLogin()
 {
   var status = document.getElementById("status");
   FB.getLoginStatus(function(response) { 
   //Conectado
  if (response.status === 'connected') {
  	console.log(response);

	window.location.href = url_after_login;
  } 
  //No autorizado para acceder a la aplicación
  else if (response.status === 'not_authorized'){
	status.innerHTML = "Por favor, tienes que autenticarte con Facebook";
  } 
  //No tiene sesión abierta en Facebook
  else {
	status.innerHTML = "No has iniciado sesión en Facebook";
  }
 });
}


//=================// CONSULTA DB //s================//
function validarUsuario(usuario){
	var xmlhttp;
	var txt,x,xx,i;
	xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			console.log(xmlhttp);
			console.log(xmlhttp.responseText);
			
			
		}
		
	}

	xmlhttp.open("POST", 'http://localhost:8000/verificaUsuario/', true);

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

//=================// fin CONSULTA DB //================//



	/*Función para el resto de páginas a las cuales sólo los usuarios auténticados tendrán permisos 
	para entrar, si el usuario no está autenticado, es enviado a la página de login (login.html) */
function getStateFromUser(){

	//En este elemento html mostraremos el estado del usuario
	var status = document.getElementById("status");
	
		FB.getLoginStatus(function(response) {
		
			//Si el usuario está conectado correctamente a nuestra aplicación
			if (response.status === 'connected')
			{
					//Token para los formularios, para evitar ataques del tipo CSRF
			        var token = response.authResponse.accessToken;
					
					/*
					De esta forma podemos acceder a la información del usuario
					Más información en: 
					https://developers.facebook.com/docs/facebook-login/permissions/v2.2?locale=es_ES
					*/
					FB.api('/me', function(response) {

						/*consulto en la base di existe este usuario*/
  						datosUsuario(response)
						// nombre del usuario
						name = response.name;
						// email del usuario
						email = response.email;
						// id del usuario
						id = response.id;
						
						// Incluimos un mensaje y la imagen del usuario
						status.innerHTML ="<div><p>"+ name + " </p>"+"<img src='//graph.facebook.com/"+id+"/picture'></div>";
					});
			}
			// De lo contrario lo enviamos a login.html
			else if(response.status === 'not_authorized')
			{
			window.location.href = url_after_logout;
			}
			// De lo contrario lo enviamos a login.html
			else
			{
			window.location.href = url_after_logout;
			}
		});
}
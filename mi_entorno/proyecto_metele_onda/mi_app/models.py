from django.db import models
from django.conf import settings

# Create your models here.


##----// **Clase RUBRO**  //-----------------------##
class Rubro(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.name
##----// **fin class**  //-----------------------##


##----// **Clase PROVINCIA**  //-----------------------##
class Provincia(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.name
##----// **fin class**  //-----------------------##


##----// **Clase PROVINCIA**  //-----------------------##
class Ciudad(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre        = models.CharField(max_length = 200)
	codigo_postal = models.CharField(max_length = 10)
	#--relacion muchos a uno con la clase Provincia--#
	#FK
	provincia = models.ForeignKey('Provincia')

	def __unicode__(self):
		return self.name
##----// **fin class**  //-----------------------##


##----// **Clase USUARIO**  //-----------------------##
class Usuario(models.Model):
	#----------// ATRIBUTOS  //--------#
	fb_id     = models.CharField(max_length = 200)
	tw_id     = models.CharField(max_length = 200)
	google_id = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.name
##----// **fin class**  //-----------------------##



##----// **Clase CALIFICACION**  //-----------------------##
class Calificacion(models.Model):
	#----------// ATRIBUTOS  //--------#
	puntaje    = models.IntegerField()
	comentario = models.TextField()
	#--relacion muchos a uno con la clase Usuario--#
	#FK
	usuario = models.ForeignKey('Usuario')
	#--relacion muchos a uno con la clase Establecimiento--#
	#FK
	establecimiento = models.ForeignKey('Establecimiento')

	#--------------// //---------------------#
	def __unicode__(self):
		return self.comentario
##----// **fin class**  //-----------------------##


##----// **Clase ESTABLECIOMIENTO**  //-----------------------##
class Establecimiento(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre    = models.CharField(max_length = 200)
	direccion = models.CharField(max_length = 200)
	latitud   = models.FloatField()
	longitud  = models.FloatField()

	#--relacion muchos a uno con la clase Establecimiento--#
	#FK
	ciudad = models.ForeignKey('Ciudad')
	#--relacion muchos a uno con la clase Rubro--#
	#FK
	rubro = models.ForeignKey('Rubro')
	
	def __unicode__(self):
		return self.name
##----// **fin class**  //-----------------------##


	


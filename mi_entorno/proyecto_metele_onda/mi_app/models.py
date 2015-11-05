from django.db import models

# Create your models here.


##----// **Clase RUBRO**  //-----------------------##
class Rubro(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre = models.CharField(max_length = 200)

	def as_json(self):
	    return dict(
	        id=self.id, nombre=self.nombre)

	def __unicode__(self):
		return self.nombre
##----// **fin class**  //-----------------------##


##----// **Clase USUARIO**  //-----------------------##
class Usuario(models.Model):
	#----------// ATRIBUTOS  //--------#
	fb_id     = models.CharField(null=True, max_length = 200)
	tw_id     = models.CharField(null=True, max_length = 200)
	google_id = models.CharField(null=True, max_length = 200)

	def __unicode__(self):
		return self.google_id
##----// **fin class**  //-----------------------##


##----// **Clase PROVINCIA**  //-----------------------##
class Provincia(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.nombre
##----// **fin class**  //-----------------------##


##----// **Clase PROVINCIA**  //-----------------------##
class Ciudad(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre        = models.CharField(max_length = 200)
	codigo_postal = models.CharField(max_length = 10)
	#--relacion muchos a uno con la clase Provincia--#
	#FK
	provincia = models.ForeignKey(Provincia, related_name='ciudades')

	def as_json(self):
	    return dict(
	        id=self.id, nombre=self.nombre,
	        codigo_postal=self.codigo_postal)

	def __unicode__(self):
		return self.nombre
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
	ciudad = models.ForeignKey(Ciudad, related_name='establecimientos')
	#--relacion muchos a uno con la clase Rubro--#
	#FK
	rubro = models.ForeignKey(Rubro, related_name='establecimientos')
	#--relacion muchos a uno con la clase Calificacion--#
	#FK 
	#calificaciones = models.Foreignkey(Calificacion)           #<<<<CONSULTAR relacion
	#Consulta 
	
	def as_json(self):
	    return dict(
	        id=self.id, nombre=self.nombre,
	        direccion=self.direccion, 
	        latitud=self.latitud,
	        longitud=self.longitud,
	        ciudad=self.ciudad.as_json(),
	        rubro=self.rubro.as_json())

	def __unicode__(self):
		return self.nombre
##----// **fin class**  //-----------------------##

##----// **Clase CALIFICACION**  //-----------------------##
class Calificacion(models.Model):
	#----------// ATRIBUTOS  //--------#
	puntaje    = models.IntegerField()
	comentario = models.TextField()

	# Consultar estas relaciones relacion!!!!! 
	usuario = models.ForeignKey(Usuario, related_name='calificaciones')
	establecimiento= models.ForeignKey(Establecimiento, related_name='calificaciones')   #<<<<CONSULTAR relacion
	#--------------// //---------------------#
	def __unicode__(self):
		return self.usuario
##----// **fin class**  //-----------------------##


	


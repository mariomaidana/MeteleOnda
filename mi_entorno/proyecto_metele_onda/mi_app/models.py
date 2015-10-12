from django.db import models

# Create your models here.


##----// **Clase RUBRO**  //-----------------------##
class Rubro(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre = models.CharField(max_length = 200)


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
##----// **Clase USUARIO**  //-----------------------##


##----// **Clase PROVINCIA**  //-----------------------##
class Provincia(models.Model):
	#----------// ATRIBUTOS  //--------#
	nombre = models.CharField(max_length = 200)


	def __unicode__(self):
		return self.name
##----// **Clase USUARIO**  //-----------------------##

	


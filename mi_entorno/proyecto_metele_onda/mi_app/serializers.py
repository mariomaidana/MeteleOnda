#serializers.py
from models import Rubro, Provincia, Usuario, Ciudad, Establecimiento, Calificacion
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer


#--//**Serializador USUARIO**//----------#
class UsuarioSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Usuario
#--//  fin Serializador  //----------#

#--//**Serializador PROVINCIA**//----------#
class ProvinciaSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Provincia 
#--//  fin Serializador  //----------#

#--//**Serializador RUBRO**//----------#
class RubroSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Rubro
		fields 	= ('id', 
		'nombre')
#--//  fin Serializador  //----------#

#--//**Serializador RUBRO**//----------#
class CiudadSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Ciudad
		fields 	= ('id', 
				'nombre')
#--//  fin Serializador  //----------#

#--//**Serializador RUBRO**//----------#
class EstablecimientoSerializer(ModelSerializer):


	class Meta:
		model = Establecimiento
		fields 	= ('id', 
			'nombre', 
			'direccion', 
			'ciudad', 
			'rubro', 
			'latitud',
			'longitud')

	
#--//  fin Serializador  //----------#

#--//**Serializador RUBRO**//----------#
class CalificacionSerializer(ModelSerializer):
	class Meta:
		model = Calificacion
		fields 	= ('id', 
			'puntaje', 
			'usuario', 
			'comentario',
			'establecimiento')

#--//  fin Serializador  //----------#
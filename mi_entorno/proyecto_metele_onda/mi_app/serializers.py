#serializers.py
from models import Rubro, Provincia, Usuario, Calificacion, Establecimiento, Ciudad
# Importar HyperlinkedModelSerializer para mostrar las urls en los modelos... personas, curso.
from rest_framework.serializers import HyperlinkedModelSerializer



#--//**Serializador RUBRO**//----------#
class RubroSerializer(HyperlinkedModelSerializer):
	class Meta:
		models = Rubro
#--//  fin Serializador  //----------#


#--//**Serializador PROVINCIA**//----------#
class ProvinciaSerializer(HyperlinkedModelSerializer):
	class Meta:
		models = Provincia 
#--//  fin Serializador  //----------#


#--//**Serializador CIUDAD**//----------#
class CiudadSerializer(HyperlinkedModelSerializer):
	class Meta:
		models = Ciudad
#--//  fin Serializador  //----------#


#--//**Serializador USUARIO**//----------#
class UsuarioSerializer(HyperlinkedModelSerializer):
	class Meta:
		models = Usuario
#--//  fin Serializador  //----------#

#--//**Serializador CALIFICACION**//----------#
class CalificacionSerializer(HyperlinkedModelSerializer):
	class Meta:
		models = Calificacion
#--//  fin Serializador  //----------#



#--//**Serializador ESTABLECIMIENTO**//----------#
class EstablecimientoSerializer(HyperlinkedModelSerializer):
	class Meta:
		models = Establecimiento
#--//  fin Serializador  //----------#



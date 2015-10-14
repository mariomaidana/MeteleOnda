#serializers.py
<<<<<<< HEAD
from models import Rubro, Provincia, Usuario, Calificacion, Establecimiento, Ciudad
# Importar HyperlinkedModelSerializer para mostrar las urls en los modelos... personas, curso.
from rest_framework.serializers import HyperlinkedModelSerializer



#--//**Serializador RUBRO**//----------#
class RubroSerializer(HyperlinkedModelSerializer):
	class Meta:
		models = Rubro
=======
from models import Rubro, Provincia, Usuario, Ciudad, Establecimiento, Calificacion
from rest_framework.serializers import HyperlinkedModelSerializer


#--//**Serializador USUARIO**//----------#
class UsuarioSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Usuario
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463
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
#--//  fin Serializador  //----------#

<<<<<<< HEAD
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


=======
#--//**Serializador RUBRO**//----------#
class CiudadSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Ciudad
#--//  fin Serializador  //----------#

#--//**Serializador RUBRO**//----------#
class EstablecimientoSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Establecimiento
#--//  fin Serializador  //----------#

#--//**Serializador RUBRO**//----------#
class CalificacionSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Calificacion
#--//  fin Serializador  //----------#
>>>>>>> ed5d3204d8f22217a1c2dd27fc3f229841f0d463

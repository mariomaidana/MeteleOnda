#serializers.py
from models import Rubro, Provincia, Usuario
from rest_framework.serializers import ModelSerializer


#--//**Serializador USUARIO**//----------#
class UsuarioSerializer(ModelSerializer):
	class Meta:
		models = Usuario
#--//  fin Serializador  //----------#


#--//**Serializador PROVINCIA**//----------#
class ProvinciaSerializer(ModelSerializer):
	class Meta:
		models = Provincia 
#--//  fin Serializador  //----------#


#--//**Serializador RUBRO**//----------#
class RubroSerializer(ModelSerializer):
	class Meta:
		models = Rubro
#--//  fin Serializador  //----------#

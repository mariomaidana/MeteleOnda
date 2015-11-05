from serializers import UsuarioSerializer, ProvinciaSerializer, RubroSerializer, CiudadSerializer, EstablecimientoSerializer, CalificacionSerializer, EstablecimientoEmbededSerializer
from models import Rubro, Provincia, Usuario, Ciudad, Establecimiento, Calificacion
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework import generics

from django.http import JsonResponse
from django.http import HttpResponse
from django.http import *
#import para la class -index
from django.views.generic import TemplateView # -index
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import Context, loader
import json
from django.db.models import Q


class RubroViewSet(ModelViewSet):
	queryset	 = 	Rubro.objects.all()
	serializer_class =	RubroSerializer

class UsuarioViewSet(ModelViewSet):
	queryset	 = 	Usuario.objects.all()
	serializer_class =	UsuarioSerializer

class ProvinciaViewSet(ModelViewSet):
	queryset	 = 	Provincia.objects.all()
	serializer_class =	ProvinciaSerializer

class CiudadViewSet(ModelViewSet):
	queryset	 = 	Ciudad.objects.all()
	serializer_class =	CiudadSerializer

class EstablecimientoViewSet(ModelViewSet):
	queryset	 = 	Establecimiento.objects.all()
	serializer_class =	EstablecimientoSerializer

	# def get_queryset(self):
	# 	queryset = Establecimiento.objects.all()
	# 	nombre = self.request.query_params.get('nombre', None)
	# 	direccion = self.request.query_params.get('direccion', None)
	# 	if nombre is not None:
	# 		queryset = queryset.filter(Q(nombre__contains=nombre) | Q(direccion__contains=direccion))
	# 	return queryset

	def list (self, request, format=None):
		establecmientos = Establecimiento.objects.all()
		
		nombre = self.request.query_params.get('nombre', None)
		direccion = self.request.query_params.get('direccion', None)
		
		if nombre is not None:
			establecmientos = establecmientos.filter(Q(nombre__contains=nombre) | Q(direccion__contains=direccion))
		
		results = [ob.as_json() for ob in establecmientos]
		return HttpResponse(json.dumps(results))
	# def post(self, request):	
	# 	print request.data
		#serializer = EstablecimientoSerializer(data=request.data)



		# data = json.loads(request.body)
		# establecimiento = data['establecimiento']

  #       if serializer.is_valid():
  #           serializer.save()
  #           return Response(serializer.data, status=status.HTTP_201_CREATED)
  #       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalificacionViewSet(ModelViewSet):
	queryset	 = 	Calificacion.objects.all()
	serializer_class =	CalificacionSerializer


	template_name = 'mi_app/calificar.html'

#---//  Vista para el index  //---------##
#class index----------------------------##
class Index(TemplateView):
	template_name = 'mi_app/base2.html'
#---------------------------------------##










#class calificar----------------------------##
class Calificar(TemplateView):
	template_name = 'mi_app/calificar.html'
#---------------------------------------##


#class altaEstablecimiento----------------------------##
class AltaEstablecimiento(TemplateView):
	template_name = 'mi_app/altaEstablecimiento.html'
#---------------------------------------##
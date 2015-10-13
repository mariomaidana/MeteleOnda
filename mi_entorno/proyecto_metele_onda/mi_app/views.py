from rest_framework.decorators import detail_route
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import *
from django.shortcuts import render_to_response,redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import Context, loader


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

class CalificacionViewSet(ModelViewSet):
	queryset	 = 	Calificacion.objects.all()
	serializer_class =	CalificacionSerializer
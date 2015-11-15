from serializers import UsuarioSerializer, ProvinciaSerializer, RubroSerializer, CiudadSerializer, EstablecimientoSerializer, CalificacionSerializer
from models import Rubro, Provincia, Usuario, Ciudad, Establecimiento, Calificacion
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route ,api_view, list_route
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

from rest_framework.response import Response
from django.db.models import Count, Avg
 


class RubroViewSet(ModelViewSet):
	queryset	 = 	Rubro.objects.all()
	serializer_class =	RubroSerializer



class UsuarioViewSet(ModelViewSet):
	queryset	 = 	Usuario.objects.all()
	serializer_class =	UsuarioSerializer
	
	#
	@list_route(methods=['post'])
	def register(request):
		
		queryset = Usuario.objects.filter(request['fb_id'])
		
		if queryset :
			serializer = UsuarioSerializer(data=request.DATA)
			if serializer.is_valid():
				#Cargo los datos del usuario
				serialized.save()
				return Response(fb,serializer.data, status=status.HTTP_201_CREATED)
			
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
			


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

@api_view(['GET'])
def getDiezMejores(request):

	establecmientos = Calificacion.objects.values('establecimiento').annotate(average_rating=Avg('puntaje')).order_by('-average_rating')[:5] 

	return HttpResponse(establecmientos)

@api_view(['GET'])
def getDiezPeores(request):

	establecmientos = Calificacion.objects.values('establecimiento').annotate(average_rating=Avg('puntaje')).order_by('average_rating')[:5] 

	return HttpResponse(establecmientos)


class CalificacionViewSet(ModelViewSet):
	queryset	 = 	Calificacion.objects.all()
	serializer_class =	CalificacionSerializer




#==========Consulta si el usuario existe! si no existe lo creo ====#
class ConsultaCreaUsuario(object):
    """
    The following mixin class may be used in order to support PUT-as-create
    behavior for incoming requests.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        usuario = self.get_object_or_none()
        serializer = self.get_serializer(usuario, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if usuario is None:
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            lookup_value = self.kwargs[lookup_url_kwarg]
            extra_kwargs = {self.lookup_field: lookup_value}
            serializer.save(**extra_kwargs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def get_object_or_none(self):
        try:
            return self.get_object()
        except Http404:
            if self.request.method == 'PUT':
                # For PUT-as-create operation, we need to ensure that we have
                # relevant permissions, as if this was a POST request.  This
                # will either raise a PermissionDenied exception, or simply
                # return None.
                self.check_permissions(clone_request(self.request, 'POST'))
            else:
                # PATCH requests where the object does not exist should still
                # return a 404 response.
                raise
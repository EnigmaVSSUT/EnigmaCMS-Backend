from cgitb import lookup
from django.shortcuts import render
from . import models as event_models
from . import serializers as event_serializers
from django.shortcuts import render
from rest_framework import generics, serializers,permissions

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser, JSONParser
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import (
        SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, 
        BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny
    )
import random
import string
from django.utils import timezone

#coustom permission_classes FOR READONLY permission for GET request
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class EventList(generics.ListCreateAPIView):
    queryset = event_models.Event.objects.all().order_by('-start_date')
    serializer_class = event_serializers.EventSerializer
    permission_classes = [IsAdminUser | ReadOnly] 

    def get_queryset(self):
        type = self.request.query_params.get('type')
        today = timezone.now().date()
        if type=='current':
            queryset = event_models.Event.objects.filter(end_date__gte=today, start_date__lte=today).order_by('-start_date')
        elif type=='upcoming':
            queryset = event_models.Event.objects.filter(start_date__gte=today).order_by('-start_date')
        elif type=='past':
            queryset = event_models.Event.objects.filter(end_date__lte=today).order_by('-start_date')
        else:
            queryset = event_models.Event.objects.all().order_by('-start_date')
        return queryset

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = event_models.Event.objects.all()
    serializer_class = event_serializers.EventSerializer
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):
        user=request.user
        if user.is_superuser==True:
            return self.partial_update(request, *args, **kwargs)
        else:
            context={}
            context["error"] = "You are not authorized to update."
            return Response(context,status=HTTP_400_BAD_REQUEST)
    def delete(self,request,*args, **kwargs):
        user=request.user
        slug=kwargs['slug']
        if user.is_superuser==True or user.is_staff==True:
            curr_domain = event_models.Event.objects.get(slug = slug)
            context={}
            context["message"]="Record deleted Successfully"
            curr_domain.delete()
            return Response(context,status=HTTP_200_OK)
        
        else:
            context={}
            context["error"] = "You are not authorized to delete."
            return Response(context,status=HTTP_400_BAD_REQUEST)

class RegisterForEventView(generics.ListCreateAPIView):
    queryset = event_models.EventRegistration.objects.all()
    serializer_class = event_serializers.EventRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        user_email = request.data.get('email')
        requested_event = event_models.Event.objects.filter(id=request.data.get('event')).first()
        print('request_event', (requested_event))
        registered_event_list = event_models.EventRegistration.objects.filter(email=user_email)
        for i in registered_event_list:
            if(i.event == requested_event):
                return Response({
                    'message': 'Already Registered'
                }, status=HTTP_400_BAD_REQUEST)
        serialized = event_serializers.EventRegistrationSerializer(data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response({
                'message': 'Request received'}, status=HTTP_200_OK)
        else:
            return Response({
                'message': serialized.errors
            }, status=HTTP_400_BAD_REQUEST)
        
from cgitb import lookup
from tkinter import EventType
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
from django.template.defaultfilters import slugify

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
        user_whatsapp_no = request.data.get('whatsapp_no')
        print(user_whatsapp_no)
        requested_event = event_models.Event.objects.filter(id=request.data.get('event')).first()
        print('request_event', (requested_event))
        registered_event_list = event_models.EventRegistration.objects.filter(email=user_email)
        for i in registered_event_list:
            if(i.event == requested_event):
                return Response({
                    'message': 'Already Registered'
                }, status=HTTP_400_BAD_REQUEST)
        registered_event_list = event_models.EventRegistration.objects.filter(whatsapp_no=user_whatsapp_no)
        for i in registered_event_list:
            if(i.event == requested_event):
                return Response({
                    'message': 'Already Registered'
                }, status=HTTP_400_BAD_REQUEST)
        serialized = event_serializers.EventRegistrationSerializer(data=request.data)
        if(serialized.is_valid()):
            serialized.save()
            return Response({
                'message': 'Registration Successful'}, status=HTTP_200_OK)
        else:
            return Response({
                'message': serialized.errors
            }, status=HTTP_400_BAD_REQUEST)

class CertificateListView(generics.ListCreateAPIView):
    queryset = event_models.Certificate.objects.all()
    serializer_class = event_serializers.CertificateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self,request,*args,**kwargs):
        context ={}
        user = request.user
        if user.is_superuser == True:
            request.data['certificate_number']=slugify(str(random.choices(string.ascii_uppercase+string.digits,k=10))+'_'+str(random.randrange(1,9182010))+'@')
            new_certificate = event_models.Certificate()
            new_certificate.name = request.data.get("name")
            new_certificate.decription = request.data.get("description")
            new_certificate.events = event_models.Event(id=request.data.get("events"))
            new_certificate.certificate_number = request.data.get("certificate_number")
            new_certificate.save()
            context["new_certificate"] = event_serializers.CertificateSerializer(new_certificate).data
            context["message"] = "New certificate created successfully"
            return Response(context,status=HTTP_200_OK)
        else:
            context["errors"]="You are not authorized to create certificate."
            return Response(context,status=HTTP_400_BAD_REQUEST)
    
class CertificateDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = event_models.Certificate.objects.all()
    serializer_class = event_serializers.CertificateSerializer
    lookup_field="certificate_number"
    def put(self,request,certificate_number,*args,**kwargs):
        context = {}
        if request.user.is_superuser ==True:
            curr_certificate = event_models.Certificate.objects.get(certificate_number = certificate_number)
            curr_certificate.name = request.data.get("name")
            curr_certificate.description = request.data.get("description")
            curr_certificate.events = event_models.Event.objects.get(id=request.data.get("events"))
            curr_certificate.save()
            context["Updated Certificate detail"] = event_serializers.CertificateSerializer(curr_certificate)
            context["message"] = 'Certificate details updated successfully.'
            return Response(context,status =HTTP_200_OK)
        else:
            context["error"] = "You are not authorized to update"
            return Response(context,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,certificate_number,*args,**kwargs):
        context={}
        if request.user.is_superuser == True:
            curr_certificate = event_models.Certificate.objects.get(certificate_number= certificate_number)
            curr_certificate.delete()
            context["message"] ="Certificate details deleted successfully."
            return Response(context,status=HTTP_200_OK)
        else:
            context["errors"] = 'You are not authorized to delete.'
            return Response(context,status = HTTP_400_BAD_REQUEST)

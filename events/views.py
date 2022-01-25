from cgitb import lookup
from django.shortcuts import render
from . import models as event_models
from . import serializers as event_serializers
from django.shortcuts import render
from rest_framework import generics, serializers

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

class EventList(generics.ListCreateAPIView):
    queryset = event_models.Event.objects.all().order_by('-start_date')
    serializer_class = event_serializers.EventSerializer

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

class EventDetail(generics.RetrieveDestroyAPIView):
    queryset = event_models.Event.objects.all()
    serializer_class = event_serializers.EventSerializer
    lookup_field = 'slug'

class RegisterForEventView(generics.ListCreateAPIView):
    queryset = event_models.EventRegistration.objects.all()
    serializer_class = event_serializers.EventRegistrationSerializer
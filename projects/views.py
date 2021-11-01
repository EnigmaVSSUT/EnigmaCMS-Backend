from django.shortcuts import render
from . import models as project_models
from . import serializers as project_serializers
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


class ProjectLlist(generics.ListCreateAPIView):
    # authentication_classes = [IsAuthenticated]
    queryset = project_models.Project.objects.all()
    serializer_class = project_serializers.ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = project_models.Project.objects.all()
    serializer_class = project_serializers.ProjectSerializer
    lookup_field = 'slug'


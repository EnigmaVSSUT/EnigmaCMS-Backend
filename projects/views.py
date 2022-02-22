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
from members import models as member_models

class ProjectLlist(generics.ListCreateAPIView):
    # authentication_classes = [IsAuthenticated]
    queryset = project_models.Project.objects.all()
    serializer_class = project_serializers.ProjectSerializer


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = project_models.Project.objects.all()
    serializer_class = project_serializers.ProjectSerializer
    lookup_field = 'slug'


class Document_list(APIView):
    def get(self,request):
        context={}
        queryset=project_models.Document.objects.filter(visibility='PUBLIC')
        serializer=project_serializers.ListDocumentSerializer
        user=request.user
        context['Visible to Public']=serializer(queryset).data        
        # if user:
        #     curr_member = member_models.Member.objects.get(user= user)
        #     if curr_member:
        #         member_document = project_models.Document.objects.filter(visibility= 'ONLY-MEMBERS')
        #         context['Visible to member'] = serializer(member_document).data
        #         return Response(context,status=HTTP_200_OK)
        return Response(context,status=HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        member=member_models.Member.objects.filter(user=request.user).first()
        context={}
        if member is not None:     
            data=request.data      
            new_doc=project_models.Document()
            new_doc.save()
            new_doc.title=data["title"]
            new_doc.created_by.add(member_models.Member.objects.get(user=request.user))
            new_doc.visibility=data["visibility"]
            #new_doc.visible_to.add(data["visible_to"])
            new_doc.project=project_models.Project.objects.get(id=data["project"])
            context['message']='New Document Created'
            new_doc.save()
            serializer=project_serializers.ListDocumentSerializer(new_doc)
            context["New Document"]=serializer.data
            return Response(context,HTTP_200_OK)
        else:
            context['message']="You are not Authorized"
            return Response(context,HTTP_400_BAD_REQUEST)

class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = project_models.Document.objects.all()
    serializer_class = project_serializers.ListDocumentSerializer
    lookup_field = 'id'

from cgitb import lookup
from django.shortcuts import render
from . import models as project_models
from . import serializers as project_serializers
from . import pagination as project_pagination
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
from django.contrib.auth.models import AnonymousUser
class ProjectLlist(generics.ListCreateAPIView):
    queryset = project_models.Project.objects.all()
    serializer_class = project_serializers.ProjectSerializer
    pagination_class = project_pagination.ProjectListPagination
    permissin_class=[IsAuthenticatedOrReadOnly]

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = project_models.Project.objects.all()
    serializer_class = project_serializers.ProjectSerializer
    permissin_class=[IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'


class Document_list(generics.ListCreateAPIView):
    def get(self,request):
        context={}
        public_documents=project_models.Document.objects.filter(visibility='PUBLIC')
        serializer=project_serializers.ListDocumentSerializer
        context['Visible to Public']=serializer(public_documents,many=True).data         
        if request.user.id!=None:
            curr_member = member_models.Member.objects.get(user= request.user)
            if curr_member:
                member_documents = project_models.Document.objects.filter(visibility= 'ONLY-MEMBERS')
                context["Visible to Members"]=serializer(member_documents,many=True).data
                private_documents=project_models.Document.objects.filter(visibility='PRIVATE', visible_to= request.user.id)
                if private_documents!=None:
                    context["Private"]=serializer(private_documents,many=True).data
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
            if new_doc.visibility=="PRIVATE":
                if 'visible_to' in data:
                    visible_to = data['visible_to']
                    visible_to = [int(i) for i in visible_to.split(',')]
                for i in visible_to :
                    new_visible_to = User.objects.get(id=i)
                    new_doc.visible_to.add(new_visible_to)
            else:
                data.pop('visible_to')
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
    permissin_class=[IsAuthenticatedOrReadOnly]
    queryset = project_models.Document.objects.all()
    serializer_class = project_serializers.UpdateDocumentSerializer
    lookup_field = 'id'
    def put(self, request, *args, **kwargs):
        user=request.user
        id=self.kwargs['id']
        if user.id!=None:
            curr_doc=project_models.Document.objects.get(id=id)
            curr_doc.created_by.add(member_models.Member.objects.get(user=user))
            return self.partial_update(request, *args, **kwargs)
        else:
            context={}
            context["error"] = "You are not authorized to update."
            return Response(context,status=HTTP_400_BAD_REQUEST)

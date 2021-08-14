from django.shortcuts import render
from . import models as member_models
from . import serializers as member_serializers
from django.shortcuts import render
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
def generate_random_string(n):
    return (''.join(random.choices(string.ascii_lowercase + string.digits, k=n)))



# Create your views here.
def home (request):
    return render('home.html')

class MemberList(generics.ListCreateAPIView):
    queryset = member_models.Member.objects.all()
    serializer_class = member_serializers.MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = member_models.Member.objects.all()
    serializer_class = member_serializers.MemberSerializer
    lookup_field = 'slug'



class AddMemberView(APIView):
    # parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        new_password = generate_random_string(7)
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = new_password
        new_user = User.objects.create(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        new_member = member_models.Member()
        new_member.user = new_user
        new_member.first_password = new_password
        new_member.description = request.data.get('description')
        new_member.linkedin = request.data.get('linkedin')
        new_member.github = request.data.get('github')
        new_member.facebook = request.data.get('facebook')
        new_member.instagram = request.data.get('instagram')
        new_member.year = request.data.get('year')
        new_member.save()

        context = {
            "message": "new member created",
            "new_password": new_password
        }
        return Response(context, status=HTTP_200_OK)




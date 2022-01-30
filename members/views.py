from django.shortcuts import render, get_object_or_404
from . import models as member_models
from . import serializers as member_serializers
from rest_framework import generics, serializers

from django.conf import settings
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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

SENDER_EMAIL = settings.EMAIL_HOST_USER
def generate_random_string(n):
    return (''.join(random.choices(string.ascii_lowercase + string.digits, k=n)))

def send_member_confirmation(member):
    context = {
        "member": member,
    }
    html_content = render_to_string("mails/member_confirmation.html", context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        "Form successfully submitted",
        text_content,
        SENDER_EMAIL,
        ['priyanshusingh1998@gmail.com', member.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

# Create your views here.
def home (request):
    return render('home.html')

class MemberList(generics.ListCreateAPIView):
    # authentication_classes = [IsAuthenticated]
    # queryset = member_models.Member.objects.all()
    serializer_class = member_serializers.MemberListSerializer

    def get_queryset(self):
        queryset = member_models.Member.objects.all()
        year_of_passing = self.request.query_params.get('year_of_passing')
        lookup_id = self.request.query_params.get('id')
        if year_of_passing:
            return queryset.filter(year_of_passing=year_of_passing)
        elif lookup_id:
            return queryset.filter(id =lookup_id)
        else:
            return queryset
    


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = member_models.Member.objects.all()
    serializer_class = member_serializers.MemberDetailSerializer
    lookup_field = 'slug'





class AddMemberView(APIView):
    # parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        # new_password = generate_random_string(7)
        new_password = 'EnigmaV'
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = new_password
        new_user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        new_member = member_models.Member()
        new_member.user = new_user
        new_member.first_name = first_name
        new_member.last_name = last_name
        new_member.email = email
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




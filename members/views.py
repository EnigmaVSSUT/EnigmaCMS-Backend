from django.shortcuts import render, get_object_or_404
from . import models as member_models
from . import serializers as member_serializers
from rest_framework import generics, serializers

from django.conf import settings
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework.generics import GenericAPIView, RetrieveAPIView
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
    serializer_class = member_serializers.MemberSerializer

    def get_queryset(self):
        queryset = member_models.Member.objects.all()
        year_of_passing = self.request.query_params.get('year_of_passing')
        if year_of_passing:
            return queryset.filter(year_of_passing=year_of_passing)
        else:
            return queryset
    


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = member_models.Member.objects.all()
    serializer_class = member_serializers.MemberSerializer
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

class ProfileView(APIView):
    authentication_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        site = request.META['HTTP_ORIGIN']
        context = {}
        user_qs = member_models.Member.objects.filter(user=request.user)
        if user_qs.exists():
            context['curr_user'] = member_serializers.MemberSerializer(user_qs[0]).data
            
        return Response(context,status=HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        content = {}
        username = request.data.get('username')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        description=request.data.get('description')
        linkedin = request.data.get('linkedin')
        github = request.data.get('github')
        facebook = request.data.get('facebook')
        instagram = request.data.get('instagram')
        twitter = request.data.get('twitter')
        codechef = request.data.get('codechef')
        geeksforgeeks = request.data.get('geeksforgeeks')
        hackerearth = request.data.get('hackerearth')
        others = request.data.get('others')
        year = request.data.get('year')
        curr_member=request.user
        if username:
            curr_member.username = username
        if email:
            curr_member.email = email
        if first_name:
            curr_member.first_name = first_name
        if last_name:
            curr_member.last_name = last_name
        if description:
            curr_member.description = description
        if linkedin:
            curr_member.linkedin = linkedin
        if github:
            curr_member.github = github
        if facebook:
            curr_member.facebook = facebook
        if instagram:
            curr_member.instagram = instagram
        if twitter:
            curr_member.twitter = twitter
        if codechef:
            curr_member.codechef = codechef
        if geeksforgeeks:
            curr_member.geeksforgeeks = geeksforgeeks
        if hackerearth:
            curr_member.hackerearth = hackerearth
        if others:
            curr_member.others = others
        if year:
            curr_member.year = year
        curr_member.save()
        content['curr_member'] = member_serializers.UserSerializer(curr_member).data
        user_qs = member_models.Member.objects.filter(user=request.user)
        if user_qs.exists():
            curr_user = user_qs[0]
            serializer = member_serializers.MemberSerializer(curr_user,data=request.data,partial=True)
            if serializer:
                context = {
                    "message":"Member Details Updated"
                }
                return Response(context,status = HTTP_200_OK)
            else:
                return Response(serializer.errors,status = HTTP_400_BAD_REQUEST)

        return Response(content,status = HTTP_200_OK)

class PartialView(GenericAPIView, UpdateModelMixin):
    permission_classes= [IsAuthenticatedOrReadOnly]
    queryset = member_models.Member.objects.all()
    serializer_class = member_serializers.MemberSerializer
    lookup_field = 'slug'
    
    def put(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)


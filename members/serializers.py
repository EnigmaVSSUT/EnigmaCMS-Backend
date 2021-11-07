from rest_framework import serializers
from . import models as member_models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        # exclude = ('password',)
        model = User

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('user', 'slug')
        model = member_models.Member




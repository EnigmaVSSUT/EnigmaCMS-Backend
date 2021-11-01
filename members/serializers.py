from rest_framework import serializers
from . import models as member_models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        # exclude = ('password',)
        model = User

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = member_models.Member




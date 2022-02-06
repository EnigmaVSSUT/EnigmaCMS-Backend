from rest_framework import serializers
from . import models as member_models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        # exclude = ('password',)
        model = User


class CreateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('user',)
        model = member_models.Member


class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('user',)
        model = member_models.Member


class MemberDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        fields = '__all__'
        model = member_models.Member


class MemberUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'description', 
            'github', 
            'linkedin', 
            'facebook', 
            'instagram', 
            'twitter', 
            'codechef', 
            'geeksforgeeks', 
            'hackerearth', 
            'profile_pic', 
            'skills', 
            'domain',
        )
        model = member_models.Member
        

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = None
        if email and password:
            if User.objects.filter(email=email).exists():
                username = User.objects.filter(email=email).first()
                user = self.authenticate(username=username, password=password)
            else:
                msg = {'detail': 'Email address is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)
            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

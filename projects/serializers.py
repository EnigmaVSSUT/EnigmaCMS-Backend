from . import models as project_models
from rest_framework import serializers
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = project_models.Project


class CreateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('time_stamp','visible_to',)
        model=project_models.Document

class ListDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=project_models.Document
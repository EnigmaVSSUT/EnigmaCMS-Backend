from . import models as project_models
from rest_framework import serializers
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = project_models.Project
        
    def to_representation(self, instance):
        req = super().to_representation(instance)
        result = {}
        for field in req:
            if field != 'tech_stack':
                result[field] = req[field]
        result['tech_stack'] = []
        if req['tech_stack'] is not None:
            tech_stack_string = req['tech_stack']
            res1 = ''.join(tech_stack_string[1:-1].split())
            res1 = res1.split(',')
            for i in res1:
                result['tech_stack'].append(i[1:-1])
        return result

class CreateDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('time_stamp','visible_to',)
        model=project_models.Document

class ListDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=project_models.Document
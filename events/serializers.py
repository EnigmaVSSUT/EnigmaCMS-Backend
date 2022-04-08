from . import models as event_models
from rest_framework import serializers
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = event_models.Event

class EventRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = event_models.EventRegistration

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = event_models.Certificate
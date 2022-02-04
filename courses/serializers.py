from django.db.models import fields
from rest_framework import serializers
from . import models as core_models
from members import models as member_models
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        exclude = ('password',)
        model = User

class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = member_models.Member

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.Tag


class ArticleTrackSerializer(serializers.ModelSerializer):
    # edition = EditionSerializer(many=True, read_only=True)
    # edition_slug = serializers.CharField()
    class Meta:
        fields = '__all__'
        model = core_models.Article

class ArticleListSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    Tag = TagSerializer(read_only=True)
    class Meta:
        # fields = '__all__'
        exclude = ('content', )
        model = core_models.Article

class ArticleSerializer(serializers.ModelSerializer):
    member = MemberSerializer(read_only=True)
    # Tag = TagSerializer(read_only=True)
    class Meta:
        fields = '__all__'
        model = core_models.Article

class TrackSerializer(serializers.ModelSerializer):
    # articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = core_models.Track

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = core_models.ArticleImage



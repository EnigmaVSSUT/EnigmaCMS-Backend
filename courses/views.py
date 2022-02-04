from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework import response
from rest_framework import status
from . import models as core_models
from . import serializers as core_serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import (
        SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, 
        BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny
    )
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse



class ArticleList(generics.ListCreateAPIView):
    queryset = core_models.Article.objects.filter(status='Published')
    serializer_class = core_serializers.ArticleListSerializer

    def get_queryset(self):
        queryset = core_models.Article.objects.filter(status='Published')
        tag_slug = self.request.query_params.get('tag')
        track_slug = self.request.query_params.get('track')
        if tag_slug is not None:
            try:
                tag = core_models.Tag.objects.get(slug=tag_slug)
                queryset = queryset.filter(tag=tag, status='Published')
            except:
                queryset = core_models.Article.objects.filter(status='Published')
        if track_slug is not None:
            try:
                track = core_models.Track.objects.get(slug=track_slug)
                queryset = track.articles.filter(status='Published')
            except:
                queryset = core_models.Article.objects.filter(status='Published')
        return queryset

class tagList(generics.ListCreateAPIView):
    queryset = core_models.tag.objects.all()
    serializer_class = core_serializers.tagSerializer

class TrackList(generics.ListCreateAPIView):
    queryset = core_models.Track.objects.filter(is_active=True).order_by('-timestamp')
    serializer_class = core_serializers.TrackSerializer

    # def get(self, request, *args, **kwargs):
    #     update_subscription()
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = core_models.Track.objects.filter(is_active=True).order_by('-timestamp')
        try:
            site = self.request.META['HTTP_ORIGIN']
            if site == 'https://club.enigmavssut.com' or site=='http://localhost:3000' or site=='http://localhost:8080':
                # update_subscription()
                queryset = core_models.Track.objects.all().order_by('-timestamp')
            
            elif site == 'https://enigmavssut.com' or site=='http://localhost:3000':
                queryset = core_models.Track.objects.filter(is_active=True).order_by('-timestamp')
            return queryset
        except:
            return queryset

class CreateArticle(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = core_serializers.ArticleTrackSerializer
    def post(self, request, *args, **kwargs):
        context = {}
        serializer = core_serializers.ArticleTrackSerializer(data=request.data)
        if serializer.is_valid():
            try:
                curr_author = core_models.Member.objects.get(user=request.user)
            except:
                return Response({"message": "You are not an author. You cannot create article"}, status=HTTP_400_BAD_REQUEST)
            this_article = serializer.save(writer=curr_author)
            context['new_article'] = serializer.data

            curr_track = this_article.track
            context['message'] = f'Article added to track {curr_track.name}'

            return Response(context, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class tagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = core_models.tag.objects.all()
    serializer_class = core_serializers.tagSerializer
    lookup_field = 'slug'

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = core_models.Article.objects.all()
    serializer_class = core_serializers.ArticleSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        site = request.META['HTTP_ORIGIN']
        print(site)
        if site != "https://club.enigmavssut.com":
            article_object = self.get_object()
            article_object.visits += 1
            article_object.save()
            
        return super().get(request, *args, **kwargs)

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = core_models.Track.objects.all()
    serializer_class = core_serializers.TrackSerializer
    lookup_field = 'slug'


class ArticlePartialUpdateView(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = core_models.Article.objects.all()
    serializer_class = core_serializers.ArticleTrackSerializer
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class TrackPartialUpdateView(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = core_models.Track.objects.all()
    serializer_class = core_serializers.TrackSerializer
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class tagPartialUpdateView(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = core_models.tag.objects.all()
    serializer_class = core_serializers.tagSerializer
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class ArticleStatusChange(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids', None)
        status = request.data.get('status', None)
        if status=='Published' or status=='Rejected':
            if not request.user.is_superuser:
                return Response({"message": f'You dont have permission to publish an article'}, status=HTTP_400_BAD_REQUEST)
        
        for id in ids:
            if id is None:
                continue
            curr_article = core_models.Article.objects.get(id=id)
            curr_article.status = status
            curr_article.save()
        return Response({"message": f'The article were marked as \"{status}\"!'}, status=HTTP_200_OK)

class ArticleImageList(generics.ListCreateAPIView):
    queryset = core_models.ArticleImage.objects.all()
    serializer_class = core_serializers.ArticleImageSerializer

class ArticleImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = core_models.ArticleImage.objects.all()
    serializer_class = core_serializers.ArticleImageSerializer
    lookup_field = 'name'

class ArticlePublishingRequests(GenericAPIView):
    def get(self, request, *args, **kwargs):
        context = {}
        context['all_draft_articles'] = core_serializers.ArticleSerializer(core_models.Article.objects.filter(status='Draft'), many=True).data
        context['all_created_articles'] = core_serializers.ArticleSerializer(core_models.Article.objects.filter(status='Created'), many=True).data
        context['all_rejected_articles'] = core_serializers.ArticleSerializer(core_models.Article.objects.filter(status='Rejected'), many=True).data
        return Response(context, status=HTTP_200_OK)

def article_image_detail(reqeust, name):
    article_img = core_models.ArticleImage.objects.get(name=name)
    ser_article_img = core_serializers.ArticleImageSerializer(article_img)
    response = HttpResponse(article_img.image.file)
    response['Content-Type'] = "image/*"
    response['Cache-Control'] = "max-age=0"
    return response





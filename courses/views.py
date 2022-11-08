from ast import Delete
from os import stat
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
from members import models as member_models

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
                queryset = core_models.Article.objects.filter(
                    status='Published')
        if track_slug is not None:
            try:
                track = core_models.Track.objects.get(slug=track_slug)
                queryset = track.articles.filter(status='Published')
            except:
                queryset = core_models.Article.objects.filter(
                    status='Published')
        return queryset.order_by('timestamp')

class TagList(generics.ListCreateAPIView):
    queryset = core_models.Tag.objects.all()
    serializer_class = core_serializers.TagSerializer

class TrackList(generics.ListCreateAPIView):
    queryset = core_models.Track.objects.filter(
        is_active=True).order_by('-timestamp')
    serializer_class = core_serializers.TrackSerializer

    # def get(self, request, *args, **kwargs):
    #     update_subscription()
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = core_models.Track.objects.filter(
            is_active=True).order_by('-timestamp')
        try:
            site = self.request.META['HTTP_ORIGIN']
            if site == 'https://club.enigmavssut.com' or site == 'http://localhost:3000' or site == 'http://localhost:8080':
                # update_subscription()
                queryset = core_models.Track.objects.all().order_by('-timestamp')

            elif site == 'https://enigmavssut.com' or site == 'http://localhost:3000':
                queryset = core_models.Track.objects.filter(
                    is_active=True).order_by('-timestamp')
            return queryset
        except:
            return queryset


class CreateArticle(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = core_serializers.CreateArticleSerializer

    def post(self, request, *args, **kwargs):
        context = {}
        data=request.data
        if 'tags' in data:
            tags = data['tags']
            tags = [int(i) for i in tags.split(',')]
            print('tags:===', tags)
        else:
            tags=[]
        data.pop('tags')
        serializer = core_serializers.CreateArticleSerializer(data=data)
        if serializer.is_valid():
            try:
                curr_author = core_models.Member.objects.get(user=request.user)
            except:
                return Response({"message": "You are not an author. You cannot create article"}, status=HTTP_400_BAD_REQUEST)
            this_article = serializer.save(member=curr_author)
            

            curr_track = this_article.track
            for t in tags:
                new_tag = core_models.Tag.objects.get(id=t)
                this_article.tags.add(new_tag)
            context['new_article'] = serializer.data
            context['message'] = f'Article added to track {curr_track.name}'

            return Response(context, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class TagDetail(APIView):
    
    def get(self, request, *args, **kwargs):
        slug=self.kwargs['slug']
        tag=core_models.Tag.objects.filter(slug=slug).first()        
        articles = core_models.Article.objects.filter(tags__in=[tag.id])
        context={
            "Data" : core_serializers.TagSerializer(tag).data,
            "Articles":core_serializers.ArticleTagSerializer(articles,many=True).data
        }
        return Response(context)    


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = core_models.Article.objects.all()
    serializer_class = core_serializers.ArticleSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        try:
            site = request.META['HTTP_ORIGIN']
            print(site)
            if site != "https://club.enigmavssut.com":
                article_object = self.get_object()
                article_object.visits += 1
                article_object.save()
        except:
            pass

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

class TagPartialUpdateView(GenericAPIView, UpdateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = core_models.Tag.objects.all()
    serializer_class = core_serializers.TagSerializer
    lookup_field = 'slug'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ArticleStatusChange(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        ids = request.data.get('ids', None)
        status = request.data.get('status', None)
        if status == 'Published' or status == 'Rejected':
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
        context['all_draft_articles'] = core_serializers.ArticleSerializer(
            core_models.Article.objects.filter(status='Draft'), many=True).data
        context['all_created_articles'] = core_serializers.ArticleSerializer(
            core_models.Article.objects.filter(status='Created'), many=True).data
        context['all_rejected_articles'] = core_serializers.ArticleSerializer(
            core_models.Article.objects.filter(status='Rejected'), many=True).data
        return Response(context, status=HTTP_200_OK)


def article_image_detail(reqeust, name):
    article_img = core_models.ArticleImage.objects.get(name=name)
    ser_article_img = core_serializers.ArticleImageSerializer(article_img)
    response = HttpResponse(article_img.image.file)
    response['Content-Type'] = "image/*"
    response['Cache-Control'] = "max-age=0"
    return response



class Articles_by_author(APIView):
    
    def get(self,request,*arg, **kwargs):
        user=request.user
        status=request.query_params
        member=member_models.Member.objects.filter(user=user).first()
        queryset = core_models.Article.objects.filter(member=member)
        status= self.request.GET.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        serializer_class = core_serializers.ArticleByAuthorSerializer(queryset,many=True)
        return Response(serializer_class.data)
      
class ArticleProperties(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        tags = core_models.Tag.objects.all()
        tracks = core_models.Track.objects.all()
        categories = core_models.CATEGORY_CHOICES
        cat = []
        for category in categories:
            cat.append({
                'value': category[0],
                'label': category[1]
            })
        context = {
            'tag': core_serializers.ArticlePropertiesTagsSerializer(tags, many=True).data,
            'track': core_serializers.ArticlePropertiesTracksSerializer(tracks, many=True).data,
            'category': cat
        }
        return Response(context)
class ArticleProperties(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        tags = core_models.Tag.objects.all()
        tracks = core_models.Track.objects.all()
        categories = core_models.CATEGORY_CHOICES
        cat = []
        for category in categories:
            cat.append({
                'value': category[0],
                'label': category[1]
            })
        context = {
            'tag': core_serializers.ArticlePropertiesTagsSerializer(tags, many=True).data,
            'track': core_serializers.ArticlePropertiesTracksSerializer(tracks, many=True).data,
            'category': cat
        }
        return Response(context)



class CreateDomain(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = core_models.Domain.objects.all()
    serializer_class = core_serializers.DomainSerializer
    def post(self,request,*args,**kwargs):
        if request.user.is_superuser == True:
            context={}
            data =request.data
            new_domain = core_models.Domain()
            new_domain.name =data['name']
            new_domain.domain_lead =  member_models.Member.objects.get(id = data['domain_lead'])
            new_domain.icon = data['icon']
            new_domain.short_description = data['short_description']
            new_domain.detailed_description = data['detailed_description']
            new_domain.created_by = member_models.Member.objects.get(user = request.user)
            new_domain.save()
            context["New_domain"] = core_serializers.DomainSerializer(new_domain).data
            context['message'] = "New domain created successfully"
            return Response(context,status=HTTP_200_OK)
        else:
            context={}
            context["error"] = "You are not authorized."
            return Response(context,status=HTTP_400_BAD_REQUEST)



class DomainDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = core_models.Domain.objects.all()
    serializer_class = core_serializers.DomainSerializer
    lookup_field = 'id'
    def put(self, request, *args, **kwargs):
        user=request.user
        if user.is_staff==True or user.is_superuser==True:
            return self.partial_update(request, *args, **kwargs)
        else:
            context={}
            context["error"] = "You are not authorized to update."
            return Response(context,status=HTTP_400_BAD_REQUEST)
    def delete(self,request,id,*args, **kwargs):
        user=request.user
        if user.is_superuser==True:
            curr_domain = core_models.Domain.objects.get(id = id)
            context={}
            context["message"]="Record deleted Successfully"
            curr_domain.delete()
            return Response(context,status=HTTP_200_OK)
        
        else:
            context={}
            context["error"] = "You are not authorized to delete."
            return Response(context,status=HTTP_400_BAD_REQUEST)
        
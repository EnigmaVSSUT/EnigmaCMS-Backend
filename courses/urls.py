from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('article-list', views.ArticleList.as_view(), name="article-list"),
    path('track-list', views.TrackList.as_view(), name="track-list"),
    path('tag-list/', views.TagList.as_view(), name='tag-list'),
    path('tag-detail/<slug>/', views.TagDetail.as_view(), name="tag-detail"),
    path('article-detail/<slug>/',
         views.ArticleDetail.as_view(), name="item_detail"),
    path('track-detail/<slug>/', views.TrackDetail.as_view(), name="track-detail"),
    path('create-article/', views.CreateArticle.as_view(), name="create-article"),
    path('edit-article/<slug>/',
         views.ArticlePartialUpdateView.as_view(), name="edit-article"),
    path('edit-track/<slug>/',
         views.TrackPartialUpdateView.as_view(), name="edit-track"),
    path('edit-tag/<slug>/', views.TagPartialUpdateView.as_view(), name="edit-tag"),

    path('article-status-update/', views.ArticleStatusChange.as_view(),
         name="article-status-update"),
    path('article-details-list/', views.ArticlePublishingRequests.as_view(),
         name="article-details-list"),
    path('article-status-update/', views.ArticleStatusChange.as_view(), name="article-status-update"),
    path('article-details-list/', views.ArticlePublishingRequests.as_view(), name="article-details-list"),
    path('article-props/', views.ArticleProperties.as_view(), name="article-prop"),



    path('article-image-list/', views.ArticleImageList.as_view(),
         name="article-image-list"),
    path('article-image-detail/<name>/',
         views.article_image_detail, name="article-image-detail"),

    path('articles-by-author/', views.Articles_by_author.as_view(),
         name='articles-by-author'),
    path('domain-detail/<int:id>/', views.DomainDetailView.as_view(),
         name='detail-domain'), 
    path('domain-list/',views.CreateDomain.as_view(),name='domain-list'),
]



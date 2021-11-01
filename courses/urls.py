from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('article-list', views.ArticleList.as_view(), name="article-list"),
    path('track-list', views.TrackList.as_view(), name="track-list"),
    path('topic-detail/<slug>/', views.TopicDetail.as_view(), name="topic-detail"),
    path('article-detail/<slug>/', views.ArticleDetail.as_view(), name="item_detail"),
    path('edition-detail/<slug>/', views.TrackDetail.as_view(), name="track-detail"),
    path('create-article/', views.CreateArticle.as_view(), name="create-article"),
    path('edit-article/<slug>/', views.ArticlePartialUpdateView.as_view(), name="edit-article"),
    path('edit-edition/<slug>/', views.TrackPartialUpdateView.as_view(), name="edit-track"),
    path('edit-topic/<slug>/', views.TopicPartialUpdateView.as_view(), name="edit-topic"),
    path('article-status-update/', views.ArticleStatusChange.as_view(), name="article-status-update"),
    path('article-details-list/', views.ArticlePublishingRequests.as_view(), name="article-details-list"),


    path('article-image-list/', views.ArticleImageList.as_view(), name="article-image-list"),
    path('article-image-detail/<name>/', views.article_image_detail, name="article-image-detail"),
]
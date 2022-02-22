from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('list', views.ProjectLlist.as_view(), name="project-list"),
    path('detail/<slug>', views.ProjectDetail.as_view(), name="project-detail"),
    path('document-list',views.Document_list.as_view(),name="document-list"),
    path('document-detail/<int:id>',views.DocumentDetail.as_view(),name="document-detail")
]
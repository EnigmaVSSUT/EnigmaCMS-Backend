from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('add', views.ProjectLlist.as_view(), name="project-list"),
    path('deatail/<slug>', views.ProjectDetail.as_view(), name="project-detail"),
]
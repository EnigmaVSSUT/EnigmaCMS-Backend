
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('member-list', views.MemberList.as_view(), name="member-list"),
    path('member-detail/<slug>/', views.MemberDetail.as_view(), name="member-detail"),
    path('create-member/', views.AddMemberView.as_view(), name="create-member"),
    path('profile-view/',views.ProfileView.as_view(), name="profile-view" ),
    path('edit-member/<slug>/',views.PartialView.as_view(),name="edit-member")
]
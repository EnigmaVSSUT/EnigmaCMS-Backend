
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.EventList.as_view(), name="event-list"),
    path('detail/<slug>', views.EventDetail.as_view(), name="event-detail"),
    path('register/', views.RegisterForEventView.as_view(), name="event-register"),
    path('certificate-list/',views.CertificateListView.as_view(),name="certificate-list"),
    path('certificate-detail/<certificate_number>',views.CertificateDetailView.as_view(),name="certificate-detail"),
]
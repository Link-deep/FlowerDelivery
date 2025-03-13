from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
]
from django.urls import path
from .views import register_view, login_view, logout_view, profile_view, edit_profile

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', edit_profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile')
]

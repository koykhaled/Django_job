from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', editProfile, name='profile_edit')
]

from django.urls import path
from .views import *


app_name = 'contact'
urlpatterns = [
    path('', sendMessage, name='contact')
]

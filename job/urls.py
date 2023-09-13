from django.urls import path
from .views import *


urlpatterns = [
    path('', jobList, name='jobs'),
    path('<int:id>', jobDetails, name='job-detail'),
]

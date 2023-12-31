from django.urls import path
from .views import *
from .api import *


app_name = 'jobs'

urlpatterns = [
    path('', jobList, name='job_list'),
    path('add', addJob, name='add_job'),
    path('<str:slug>', jobDetails, name='job_detail'),

    # api urls

    path('api/jobs', jobListApi, name='jobListApi')
]

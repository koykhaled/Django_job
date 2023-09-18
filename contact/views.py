from django.shortcuts import render, HttpResponse

# Create your views here.


def sendMessage(request):
    return HttpResponse("hello")

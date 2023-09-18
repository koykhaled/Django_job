from django.shortcuts import render, HttpResponse
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def sendMessage(request):
    info = Info.objects.first()
    if request.method == "POST":
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
        print(subject)
    return render(request, 'contact/contact.html', {'info': info})

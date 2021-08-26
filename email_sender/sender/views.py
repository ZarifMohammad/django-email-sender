from django import forms
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from . import forms
# Create your views here.

def subscribe(request):
    sub = forms.Subscribe()

    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)

        subject = str(sub['Subject'].value())
        message = str(sub['Message'].value())
        recepient = str(sub['Email'].value())

        send_mail(subject , message , settings.EMAIL_HOST_USER , [recepient] , fail_silently=False)
        return render(request , 'sender/success.html' , {'recepient' : recepient})

    return render(request , 'sender/index.html' , {'form' : sub})


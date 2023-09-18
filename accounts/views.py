from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('accounts:profile')

    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request, 'accounts/profile.html', {'profile': profile})


def editProfile(request):

    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_profile = profile_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect('accounts:profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'profile': profile_form, 'user': user_form})

from django.shortcuts import render, redirect
from app.models import Profile


def base(request):
    return render(request, 'base.html')


def profile(request):
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})

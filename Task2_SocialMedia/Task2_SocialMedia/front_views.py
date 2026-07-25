from django.shortcuts import render, redirect

def base(request):
     return render(request, 'base.html')
def login(request):
     return render(request, 'login.html')
def register(request):
     return render(request, 'register.html')
def hearder(request):
     return render(request, 'hearder.html')
def home(request):
     return render(request, 'home.html')
def navbar(request):
     return render(request, 'navbar.html')
def profile(request):
     return render(request, 'profile.html')
def massage(request):
     return render(request, 'massage.html')
def reels(request):
     return render(request, 'reels.html')
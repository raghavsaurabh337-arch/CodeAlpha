from django.shortcuts import render
from .models import Profile
from rest_framework import serializers
from .serailizers import ProfileSerializer

# Create your views here.
def profile_list(request):
     profiles = Profile.objects.all()
     serializer = ProfileSerializer(profiles, many=True)
     con={
          'profiles': profiles

     }
     return render(request,"profile.html",con)
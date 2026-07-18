from django.shortcuts import render ,redirect
from .models import Register
from .serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.decorators import api_view
@api_view(["GET", "POST", "PUT", "DELETE"])



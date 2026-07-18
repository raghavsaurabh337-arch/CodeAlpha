from .models import Register
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('full_name', 'email', 'mobile', 'password', 'confirm_password', 'terms')     
from django.db import models

class Register(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    terms = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
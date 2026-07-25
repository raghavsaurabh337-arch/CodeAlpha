from django.db import models

# Create your models here.
from django.db import models


class Profile(models.Model):
     name = models.CharField(max_length=100)
     image = models.ImageField(upload_to="profile/")
     bio = models.TextField(blank=True)
     followers=models.IntegerField(default=0)
     following=models.IntegerField(default=0)



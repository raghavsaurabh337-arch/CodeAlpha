

from django.contrib import admin
from .models import Profile

# Register your models here
admin.site.register(Profile)
class profileAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'image', 'bio','followers',' following']

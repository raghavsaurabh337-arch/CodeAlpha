

from django.contrib import admin
from .models import Profile,Post,Comment

# Register your models here
admin.site.register(Profile)
class profileAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'image', 'bio','followers',' following']

admin.site.register(Post)
class postAdmin(admin.ModelAdmin):
     list_display = ['id', 'user', 'image', 'caption', 'created_at', 'likes']
admin.site.register(Comment)  
class commentAdmin(admin.ModelAdmin):
     list_display = ['id', 'post', 'user', 'comment', 'created_at']


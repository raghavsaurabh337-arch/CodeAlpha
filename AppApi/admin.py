from django.contrib import admin
from .models import Register

# Register your models here.

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","email","mobile","created_at",'password')

    search_fields = ("full_name","email","mobile", )

    list_filter = ( "created_at",    )

    ordering = ("-created_at",)

    list_per_page = 10
    
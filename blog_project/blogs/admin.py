from django.contrib import admin
from .models import CustomUserModel, BlogModel

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(BlogModel)

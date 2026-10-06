from django.contrib import admin
from .models import CustomUserModel, BookModel

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(BookModel)
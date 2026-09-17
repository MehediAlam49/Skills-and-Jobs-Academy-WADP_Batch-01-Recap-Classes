from django.contrib import admin
from Recipe.models import *
# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(RecipeModel)
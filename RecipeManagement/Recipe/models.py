from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):

    def __str__(self):
        return f'{self.username}'


class RecipeModel(models.Model):
    name=models.CharField(max_length=100, null=True)
    ingredients=models.TextField(null=True)
    instructions=models.TextField(null=True)
    recipe_image=models.ImageField(upload_to='media/recipe', null=True)
    creator=models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, null=True, related_name='recipes')
    description=models.TextField(null=True)
    created_at=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name}'
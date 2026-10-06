from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username

# title,author name,description,book image,create at,update at
class BookModel(models.Model):
    title = models.CharField(max_length=100,null=True)
    author_name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    book_image = models.ImageField(upload_to='book_images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title
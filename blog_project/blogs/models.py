from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Name, Email, Contact Number
class CustomUserModel(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username


# Content Title, Author Name, Author Email, Description, Created_At
class BlogModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    author_name = models.CharField(max_length=100, null=True)
    author_email = models.EmailField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
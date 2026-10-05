from django import forms
from .models import CustomUserModel, BlogModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'full_name', 'contact_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'email', 'full_name', 'contact_number')


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'author_name', 'author_email', 'description']
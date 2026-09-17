from django import forms
from Recipe.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass

class RecipeForm(forms.ModelForm):
    class Meta:
        model=RecipeModel
        fields='__all__'
        exclude=['creator']
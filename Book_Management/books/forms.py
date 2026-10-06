from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUserModel, BookModel

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'full_name', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'
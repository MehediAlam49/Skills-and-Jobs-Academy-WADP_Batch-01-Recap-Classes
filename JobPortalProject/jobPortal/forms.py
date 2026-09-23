from django import forms
from django.contrib.auth.forms import UserCreationForm
from jobPortal.models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model=CustomUserModel
        fields=['username', 'display_name', 'email', 'user_type', 'password1', 'password2']


class RecruiterProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=RecruiterProfileModel
        fields='__all__'
        exclude=['recruiter']


class SeekerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=SeekerProfileModel
        fields='__all__'
        exclude=['seeker']
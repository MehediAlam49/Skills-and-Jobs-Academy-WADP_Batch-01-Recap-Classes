from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm, BlogForm
from .models import CustomUserModel, BlogModel

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
        'form_title': 'Register',
        'form_submit_text': 'Register',
        'auth_switch_text': 'Already have an account? Log in',
        'auth_switch_link_text': 'Log in'
    }
    return render(request, 'register.html', context)
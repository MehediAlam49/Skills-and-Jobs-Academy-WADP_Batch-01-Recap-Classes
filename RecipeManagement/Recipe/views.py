from django.shortcuts import render,redirect,get_object_or_404
from Recipe.models import *
from Recipe.forms import *
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def Registration_page(request):
    if request.method== 'POST':
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('Login_page')

    form_data=RegistrationForm()
    context={
        'form_data':form_data,
        'form_title': 'Resister Form',
        'form_btn': 'Register'
    }
    return render(request, 'master/base-form.html',context)

def Login_page(request):
    if request.method=='POST':
        form_data=LoginForm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            if user:
                login(request, user)
                return redirect('home')

    form_data=LoginForm()

    context={
            'form_data':form_data,
            'form_title': 'Login Form',
            'form_btn': 'Login'
        }
    return render(request, 'master/base-form.html',context)


def logout_page(request):
    logout(request)
    return redirect('Login_page')



def home(request):
    return render(request, 'home.html')
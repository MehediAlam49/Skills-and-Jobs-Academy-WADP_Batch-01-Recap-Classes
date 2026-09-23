from django.shortcuts import render,redirect,get_object_or_404
from jobPortal.models import *
from jobPortal.forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_view')

    form_data=RegistrationForm()
    context={
        'form_data': form_data,
        'form_title': 'Register Here',
        'form_btn': 'Register'
    }
    return render(request, 'master/base-form.html', context)

def login_view(request):
    if request.method=='POST':
        form_data=AuthenticationForm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            if user:
                login(request, user)
                return redirect('dashboard_view')

    form_data=AuthenticationForm()
    context={
        'form_data': form_data,
        'form_title': 'Login Here',
        'form_btn': 'Login'
        }
    return render(request, 'master/base-form.html', context)

def logout_view(request):
    logout(request)
    return redirect('login_view')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def profile_view(request):
    return render(request, 'profile.html')

def update_profile_view(request):
    current_user=request.user
    try:
        profile_data=RecruiterProfileModel.objects.get(recruiter=current_user)
    except:
        profile_data=None

    if current_user.user_type== 'Recruiter':
        if request.method=='POST':
            form_data=RecruiterProfileUpdateForm(request.POST, request.FILES, instance=profile_data)
            if form_data.is_valid():
                data=form_data.save(commit=False)
                data.recruiter = current_user
                data.save()
                return redirect('profile_view')
        form_data=RecruiterProfileUpdateForm(instance=profile_data)
    else:
        try:
            profile_data=SeekerProfileModel.objects.get(seeker=current_user)
        except:
            profile_data=None
        if request.method=='POST':
            form_data=SeekerProfileUpdateForm(request.POST, request.FILES, instance=profile_data)
            if form_data.is_valid():
                data=form_data.save(commit=False)
                data.seeker = current_user
                data.save()
                return redirect('profile_view')
        form_data=SeekerProfileUpdateForm(instance=profile_data)

    context={
        'form_data': form_data,
        'form_title': 'Update profile info page',
        'form_btn': 'update profile'
        }
    return render(request, 'master/base-form.html', context)



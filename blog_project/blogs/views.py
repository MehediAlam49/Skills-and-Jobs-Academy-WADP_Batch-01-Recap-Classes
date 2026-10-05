from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, UserChangeForm, BlogForm, LoginForm
from .models import CustomUserModel, BlogModel

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form_data = RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    
    form_data = RegistrationForm()

    context = {
        'form_data': form_data,
        'form_title': 'Register',
        'form_submit_text': 'Register',
        'auth_switch_text': 'Already have an account? Log in',
        'auth_switch_link_text': 'Log in',
        'auth_switch_link': 'login'
        
    }
    return render(request, 'master/base-form.html', context)

def login_view(request):
    if request.method == 'POST':
        form_data = LoginForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page.
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    form_data = LoginForm()

    context = {
        'form_data': form_data,
        'form_title': 'Login',
        'form_submit_text': 'Login',
        'auth_switch_text': "Don't have an account? Register",
        'auth_switch_link_text': 'Register',
        'auth_switch_link': 'register'
    }
    return render(request, 'master/base-form.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def UpdateProfile_view(request):
    user = request.user
    password = user.password  # Store the current password
    if request.method == 'POST':
        form_data = UserChangeForm(request.POST, instance=user)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form_data = UserChangeForm(instance=user)

    context = {
        'form_data': form_data,
        'form_title': 'My Profile',
        'form_submit_text': 'Update Profile',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

@login_required
def home_view(request):
    blogs = BlogModel.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'home.html', context)

@login_required
def user_list_view(request):
    users = CustomUserModel.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'user_list.html', context)

@login_required
def blog_create_view(request):
    if request.method == 'POST':
        form_data = BlogForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Blog created successfully.')
            return redirect('home')
    else:
        form_data = BlogForm()

    context = {
        'form_data': form_data,
        'form_title': 'Create Blog',
        'form_submit_text': 'Create',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def blog_update_view(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    if request.method == 'POST':
        form_data = BlogForm(request.POST, instance=blog)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Blog updated successfully.')
            return redirect('home')
    else:
        form_data = BlogForm(instance=blog)

    context = {
        'form_data': form_data,
        'form_title': 'Update Blog',
        'form_submit_text': 'Update',
    }
    return render(request, 'master/base-form.html', context)

@login_required
def blog_delete_view(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted successfully.')
    return redirect('home')

@login_required
def blog_detail_view(request, blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog_detail.html', context)

@login_required
def blog_list_view(request):
    blogs = BlogModel.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog_list.html', context)

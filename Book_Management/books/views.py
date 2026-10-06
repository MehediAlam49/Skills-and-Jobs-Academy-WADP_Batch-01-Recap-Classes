from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm,LoginForm,BookForm
from .models import BookModel

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = RegistrationForm()
    context = {
        'form_data': form,
        'form_title': 'Register',
        'form_submit_text': 'Register',
        'auth_switch_text': 'Already have an account? Login',
        'auth_switch_link': 'login',
        'auth_switch_link_text': 'Login'
    }
    return render(request, 'master/base-form.html', context)

def login_view(request):
    if request.method == 'POST':
        form_data = LoginForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, 'You are Successfully Loged in.')
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

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def home_view(request):
    books = BookModel.objects.all()
    context = {
        'books': books
    }
    return render(request, 'home.html', context)

@login_required
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully.')
            return redirect('books')
        else:
            messages.error(request, 'Failed to add book. Please check the form for errors.')
    else:
        form = BookForm()
    
    context = {
        'form_data': form,
        'form_title': 'Add Book',
        'form_submit_text': 'Add Book'
    }
    return render(request, 'master/base-form.html', context)

@login_required
def edit_book_view(request, book_id):
    book = BookModel.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully.')
            return redirect('books')
        else:
            messages.error(request, 'Failed to update book. Please check the form for errors.')
    else:
        form = BookForm(instance=book)
    
    context = {
        'form_data': form,
        'form_title': 'Edit Book',
        'form_submit_text': 'Update Book'
    }
    return render(request, 'master/base-form.html', context)

@login_required
def delete_book_view(request, book_id):
    book = BookModel.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully.')
    return redirect('books')
    

@login_required
def book_detail_view(request, book_id):
    book = BookModel.objects.get(id=book_id)
    context = {
        'book': book
    }
    return render(request, 'book_details.html', context)

@login_required
def book_list_view(request):
    books = BookModel.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context)
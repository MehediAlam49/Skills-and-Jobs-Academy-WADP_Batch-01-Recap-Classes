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
    return render(request, 'register.html', {'form': form})
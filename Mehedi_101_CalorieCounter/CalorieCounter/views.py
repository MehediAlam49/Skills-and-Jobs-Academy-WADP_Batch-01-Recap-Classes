from django.shortcuts import render,redirect
from datetime import date
from django.db.models import Sum, Count
from CalorieCounter.models import *
from CalorieCounter.forms import *
from django.contrib.auth import login,logout

# Create your views here.
def register_page(request):
    if request.method=='POST':
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('login_page')


    form_data=RegistrationForm()

    context={
        'form_data': form_data,
        'form_heading':'Registration Form',
        'form_btn': 'Signup',
    }
    return render(request, 'master/base-form.html',context)

def login_page(request):
    if request.method=='POST':
        form_data=LoginForm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            login(request, user)
            return redirect('dashboard')


    form_data=LoginForm()
    context={
        'form_data': form_data,
        'form_heading':'Login Form',
        'form_btn': 'Signin',
        }
    return render(request, 'master/base-form.html',context)

def logout_page(request):
    logout(request)
    return redirect('login_page')

def dashboard(request):
    try:
        current_user = request.user
        bmr = round(request.user.user_info.bmr, 2)
    except:
        current_user=None
        bmr= 0

    today=date.today()
    today_consumed_data= ConsumedCalorie.objects.filter(
        consumed_by=current_user,
        created_at=today
    )
    total_consumed_calories=today_consumed_data.aggregate(
        total_calorie=Sum('calorie'),
        total_count=Count('calorie')
    )
    total_calorie=total_consumed_calories['total_calorie']

    try:
        less_more=bmr - total_calorie
    except:
        less_more= 0

    try:
        if bmr > total_calorie:
                suggestion = 'Eat More'
        else:
            suggestion= 'Eat less'
    except:
        bmr= 0
        total_calorie=0
        suggestion=''

    context={
        'required_calorie': bmr,
        'today_consumed_data':today_consumed_data,
        'consumed_calores': total_calorie,
        'total_count': total_consumed_calories['total_count'],
        'less_more': less_more,
        'suggestion': suggestion
    }

    return render(request, 'dashboard.html',context)

def profile_page(request):
    return render(request, 'profile.html')

def update_profile(request):
    try:
        current_user=request.user.user_info
    except:
        current_user=None

    if request.method=='POST':
        form_data=ProfileUpdateForm(request.POST, instance=current_user)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.user= request.user
            weight=data.weight
            height=data.height
            age=data.age
            if data.gender== 'Male':
                #BMR= 66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)
                bmr_calculate= 66.47+(13.75 * weight) + (5.003 * height) - (6.755 * age)
            else:
                #BMR=655.1+(9.563 x weight in kg)+(1.850 xheight in cm) - (4.676 x age in years)
                bmr_calculate= 655.1 + (9.563 *weight) + (1.850 * height) - (4.676 * age)

            data.bmr=bmr_calculate
            data.save()
            return redirect('profile_page')

    form_data=ProfileUpdateForm(instance=current_user)
    context={
        'form_data':form_data,
        'form_heading':'Update profile Form',
        'form_btn': 'Update',
    }
    return render(request, 'master/base-form.html',context)

def consumed_calorie(request):
    consumed_data=ConsumedCalorie.objects.filter(consumed_by=request.user)
    context={
        'consumed_data':consumed_data
    }
    return render(request, 'cosumed_calorie.html',context)

def add_calorie(request):
    if request.method=='POST':
        form_data=ConsumedCalorieForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.consumed_by= request.user
            data.save()
            return redirect('consumed_calorie')

    form_data=ConsumedCalorieForm()
    context={
        'form_data': form_data,
        'form_heading':'Add consumed Calorie',
        'form_btn': 'Add Calorie',
    }
    return render(request, 'master/base-form.html', context)

def edit_calorie(request,id):
    try:
        data=ConsumedCalorie.objects.get(id=id)
    except:
        data=None
    if request.method=='POST':
        form_data=ConsumedCalorieForm(request.POST, instance=data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.consumed_by= request.user
            data.save()
            return redirect('consumed_calorie')
    
    form_data=ConsumedCalorieForm(instance=data)
    context={
        'form_data': form_data,
        'form_heading':'Update Calorie',
        'form_btn': 'Update',
    }
    return render(request, 'master/base-form.html',context)

def delete_calorie(request,id):
    try:
        data=ConsumedCalorie.objects.get(id=id)
        data.delete()
    except:
        data=None
    return redirect('consumed_calorie')
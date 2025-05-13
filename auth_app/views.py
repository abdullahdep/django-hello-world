from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .middlewares import auth, guest
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        grade = request.POST.get('grade')

        # Check if any field is empty
        if not all([username, password1, password2, fullname, email, grade]):
            messages.error(request, 'All fields are required')
            return redirect('register')

        try:
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                    return redirect('register')
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email
                )
                profile = Profile.objects.create(
                    user=user,
                    fullname=fullname,
                    grade=grade,
                    email=email
                )
                messages.success(request, 'Registration successful! Please login.')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match')
                return redirect('register')
        except IntegrityError:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect('register')
    
    return render(request, 'auth/register.html')

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# logorusr = 'login/sign'
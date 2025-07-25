from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .middlewares import auth, guest
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from pages.models import Subject , MCQTestScore


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
            return redirect('/')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form}) 

@login_required(login_url='login')
def dashboard_view(request):
    user = request.user
    subjects = Subject.objects.all()

    subject_data = []
    for subject in subjects:
        scores = MCQTestScore.objects.filter(user=user, subject=subject).order_by('-created_at')
        if scores.exists():
            total_attempts = scores.count()
            average_score = sum(score.score_percentage for score in scores) / total_attempts
            
        else:
            total_attempts = 0
            average_score = 0

        subject_data.append({
            'subject': subject,
            'scores': scores,
            'average_score': round(average_score, 2),
            'total_attempts': total_attempts
        })
        

    return render(request, 'dashboard.html' , {'subject_data': subject_data})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    # Get list of grades for the dropdown
    grades = range(9, 13)  # Adjust range as needed
    
    context = {
        'user': request.user,
        'grades': grades,
    }
    return render(request, 'Profile/profile.html', context)

@login_required
def profile_update(request):
    if request.method == 'POST':
        try:
            # Get or create profile
            profile, created = Profile.objects.get_or_create(user=request.user)
            
            # Update profile fields
            profile.fullname = request.POST.get('fullname')
            profile.email = request.POST.get('email')
            profile.grade = request.POST.get('grade')
            profile.save()
            
            # Update user email if it has changed
            if request.user.email != request.POST.get('email'):
                request.user.email = request.POST.get('email')
                request.user.save()
            
            messages.success(request, 'Profile updated successfully!')
            
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
        
        return redirect('profile')

    return redirect('profile')
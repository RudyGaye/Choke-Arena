from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from Techniques_Library.models import Technique
from Training_Plans.models import TrainingPlan
from django.contrib.auth import get_user_model

User = get_user_model()

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                next_url = request.GET.get('next', 'home_index') 
                return redirect(next_url)
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def profil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profil')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profil.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Registration successful')
                return redirect('home_index')
            else:
                messages.error(request, 'Error logging in after signup')
        else:
            messages.error(request, 'Error in form submission. Please correct the errors.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def user_followed_items(request):
    """
    Display the items (techniques and training plans) followed by the user.
    Requires the user to be logged in.
    """
    user = request.user
    techniques = user.library_techniques.all()
    training_plans = user.library_plans.all()
    return render(request, 'user_followed_items.html', {
        'techniques': techniques,
        'training_plans': training_plans
    })

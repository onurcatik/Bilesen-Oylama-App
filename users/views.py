from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.is_active = False  # User is not active until admin activation
            new_user.save()
            send_mail(
                'Account Activation Required',
                'Please activate your account via admin approval.',
                settings.EMAIL_HOST_USER,
                [new_user.email],
                fail_silently=False,
            )
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
"""
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.is_active = False  # User is not active until admin activation
            new_user.save()
            
            # Send email to the user
            send_mail(
                'Account Activation Required',
                'Please activate your account via admin approval.',
                settings.EMAIL_HOST_USER,
                [new_user.email],
                fail_silently=False,
            )

            # Send email to the admin
            admin_email = settings.ADMIN_EMAIL
            send_mail(
                'New User Registration',
                f'A new user has registered with the username: {new_user.username}. Please review and activate the account.',
                settings.EMAIL_HOST_USER,
                [admin_email],
                fail_silently=False,
            )

            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
"""

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    return render(request, 'users/login.html')


def home(request):
    return render(request, 'users/home.html')

@staff_member_required
def custom_admin_view(request):
    context = {}
    return render(request, 'users/admin.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')
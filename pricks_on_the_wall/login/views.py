from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt


def login_index(request):
    return render(request, 'login_registration/login_register.html')


def register_user(request):
    errors = User.objects.validate_user(request)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            user_name=user_name,
            email=email,
            password=password
        )
        new_user.save()
        return redirect(f'/thewall/{new_user.id}')


def login_user(request):
    errors = User.objects.validate_login(request)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    email = request.POST.get('email')
    user = User.objects.filter(email=email)
    if user:
        return redirect(f'/thewall/{user[0].id}')

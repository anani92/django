from django.shortcuts import render, redirect
from .models import User, UserManger
from django.contrib import messages
import bcrypt
# Create your views here.


def index(request):
    return render(request, 'registration.html')


def register_user(request):
    errors = User.objects.validate_user(request)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        new_user.save()
        request.session['email'] = email
        return redirect('/success')


def login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.filter(email=email)
    if user:
        if bcrypt.checkpw(password.encode(), user[0].password.encode()):
            return redirect('/success')
        else:
            return redirect('/')
    else:
        print('User does not exist')
        return redirect('/')


def success(request):
    email = request.session['email']
    user = User.objects.filter(email=email)
    context = {
        'user': user[0]
    }
    return render(request, 'success.html', context)


def logout(request):
    request.session.clear()
    return redirect('/')

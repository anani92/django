from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Users


def index(request):
    context = {
        'users': Users.objects.all()
    }
    return render(request, 'index.html', context)


def add_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email_address = request.POST['email']
    age = request.POST['age']
    Users.objects.create(first_name=first_name,
                         last_name=last_name, email=email_address, age=age)
    print(Users.objects.all())
    return redirect('/')

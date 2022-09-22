from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('placeholder for users to create a new record')


def login(request):
    return HttpResponse('placeholder for user to login')


def new_user(request):
    return redirect('/')


def all_users(request):
    return HttpResponse('place holder to display users')

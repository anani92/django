from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('placeholder for surveys created')


def new_surveys(request):
    return HttpResponse('place holder for users to add new survey')

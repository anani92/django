from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import *
# Create your views here.


def main(request):
    dojos = Dojos.objects.all()
    ninjas = Ninjas.objects.all()
    context = {
        'dojos': dojos,
        'ninjas': ninjas,
    }
    return render(request, 'dojos_ninjas/index.html', context)


def add_dojo(request):
    dojo_name = request.POST['dojo_name']
    dojo_city = request.POST['dojo_city']
    dojo_state = request.POST['dojo_state']
    Dojos.objects.create(
        name=dojo_name,
        city=dojo_city,
        state=dojo_state
    )

    return redirect('/')


def add_ninja(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    this_dojo = Dojos.objects.get(id=request.POST['dojo'])

    Ninjas.objects.create(
        first_name=first_name,
        last_name=last_name,
        dojo=this_dojo
    )

    return redirect('/')

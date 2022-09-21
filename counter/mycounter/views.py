# from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render, redirect



# Create your views here.
def show_counter(request):
    if 'times' not in request.session:
        request.session['times'] = 0
        request.session['visits'] = 0
    else:
        request.session['times'] += 1
        request.session['visits'] += 1
    # if 'visits'  in request.session:
    #     request.session['visits'] += 1
    # else:
    #     request.session['visits'] += 0

    # context = {
    #     'times': request.session['times'],
    #     'visits': request.session['visits'],
    # }

    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')

def add_two(request):
    request.session['times'] += 1
    return redirect('/')

def specify_counter(request):
    request.session['times'] += int(request.POST['count'])-1
    return redirect('/')




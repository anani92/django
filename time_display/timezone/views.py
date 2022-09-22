from time import strftime, localtime
from django.shortcuts import render
def time(request):
  request.session['hello']
  context = {
    'time': strftime('%Y-%b-%d %H:%M %p', localtime())
  }
  return render(request, 'index.html', context)

from time import strftime, localtime
from django.shortcuts import render
def time(request):
  context = {
    'time': strftime('%Y-%b-%d %H:%M %p', localtime())
  }
  return render(request, 'index.html', context)

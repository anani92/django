from django.shortcuts import render, redirect


def survey(request):
    return render(request, 'survey.html')


def result(request):
    context = {
        'name': request.POST['name'],
        'user_email': request.POST['email'],
        'language': request.POST['language'],
        'comment': request.POST['comment'],
        'location': request.POST['location'],
        'gender': request.POST['gender'],
    }
    return render(request, 'result.html', context)


def back(request):
    return redirect('/')

from django.shortcuts import render, redirect
from .models import Courses
# Create your views here.


def show_courses(request):
    context = {
        'courses': Courses.objects.all(),
    }
    return render(request, 'courses.html', context)


def add_course(request):
    name = request.POST.get('course_name')
    description = request.POST.get('description')
    new_course = Courses.objects.create(
        name=name,
        description=description
    )
    new_course.save()
    return redirect('/')


def confirm_delete(request, id):
    course = Courses.objects.get(id=id)
    context = {
        'course': course
    }

    return render(request, 'confirm_delete.html', context)


def destroy(request, id):
    course_to_delete = Courses.objects.get(id=id)
    course_to_delete.delete()
    return redirect('/')

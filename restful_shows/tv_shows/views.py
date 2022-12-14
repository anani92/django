from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Shows


def all_shows(request):
    context = {
        'shows': Shows.objects.all(),
    }
    return render(request, 'shows.html', context)


def new_show(request):
    return render(request, 'new_show.html')


def create_new_show(request):
    errors = Shows.objects.show_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        title = request.POST.get('show_title')
        net_work = request.POST.get('net_work')
        release_date = request.POST.get('release_date')
        description = request.POST.get('desc')
        new_show = Shows.objects.create(
            title=title,
            network=net_work,
            release_date=release_date,
            description=description
        )
        new_show.save()
        # new_show = Shows.objects.last()
        return redirect(f'/new/{new_show.id}')


def view_show(request, id):
    show = Shows.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'view_show.html', context)


def view_show_to_edit(request, id):
    show = Shows.objects.get(id=id)
    context = {
        'show': show
    }
    return render(request, 'edit_show.html', context)


def edit_show(request, id):
    show = Shows.objects.get(id=id)
    errors = Shows.objects.show_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/{show.id}/edit')
    else:
        edited_title = request.POST.get('show_title')
        edited_net_work = request.POST.get('net_work')
        edited_release_date = request.POST.get('release_date')
        edited_discription = request.POST['desc']
        show.title = edited_title
        show.network = edited_net_work
        show.release_date = edited_release_date
        show.description = edited_discription
        show.save()
        return redirect(f'/{show.id}/edit')


def delete_show(request, id):
    show_to_delete = Shows.objects.get(id=id)
    show_to_delete.delete()
    return redirect('/')

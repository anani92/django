from multiprocessing import context
from django.shortcuts import render, redirect
from . models import *


def book_index(request):
    context = {
        'books': Books.objects.all(),
    }
    return render(request, 'authors_and_books/add_book.html', context)


def add_book(request):
    book_title = request.POST['book_title']
    desc = request.POST['book_desc']
    Books.objects.create(title=book_title, desc=desc)
    return redirect('/')


def show_book(request, id):
    book = Books.objects.get(id=id)
    context = {
        'book': book,
        'authors': Authors.objects.all(),
    }
    return render(request, 'authors_and_books/view_book.html', context)


def author_to_book(request, id):
    author_id = request.POST.get('author_to_book')
    print(author_id)
    author = Authors.objects.get(id=author_id)
    book = Books.objects.get(id=id)
    author.books.add(book)
    print(author.books.all())
    return redirect(f'/book/{id}')


def author_index(request):
    context = {
        'authors': Authors.objects.all(),
    }
    return render(request, 'authors_and_books/add_author.html', context)


def add_author(request):
    print(request.POST['first_name'])
    firstname = request.POST['first_name']
    lastname = request.POST['last_name']
    notes = request.POST['notes']
    Authors.objects.create(
        first_name=firstname,
        last_name=lastname,
        notes=notes,
    )
    return redirect('/authors')


def show_author(request, id):
    author = Authors.objects.get(id=id)
    context = {
        'author': author,
        'books': Books.objects.all(),
    }
    return render(request, 'authors_and_books/view_author.html', context)


def add_book_to_author(request, id):
    book_id = request.POST.get('book_to_author')
    print(book_id)
    book = Books.objects.get(id=book_id)
    author = Authors.objects.get(id=id)
    author.books.add(book)
    return redirect(f'/author/{author.id}')

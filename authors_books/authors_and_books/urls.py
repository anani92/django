from django.urls import path
from . import views
urlpatterns = [
    path('', views.book_index),
    path('add_book', views.add_book),
    path('author_to_book/<int:id>', views.author_to_book),
    path('book/<int:id>', views.show_book),
    path('authors', views.author_index),
    path('add_authors', views.add_author),
    path('add_book_to_author/<int:id>', views.add_book_to_author),
    path('author/<int:id>', views.show_author),

]

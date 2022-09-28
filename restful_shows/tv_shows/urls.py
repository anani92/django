from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_shows),
    path('new', views.new_show),
    path('create_new', views.create_new_show),
    path('new/<int:id>', views.view_show),
    path('<int:id>/edit', views.view_show_to_edit),
    path('edit/<int:id>', views.edit_show),
    path('delete/<int:id>', views.delete_show),
]

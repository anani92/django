from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_courses),
    path('add_course', views.add_course),
    path('destroy/<int:id>', views.confirm_delete),
    path('delete/<int:id>', views.destroy)
]

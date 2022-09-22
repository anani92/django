from django.urls import path
from . import views

app_name = 'surveys'

urlpatterns = [
    path('', views.index, name='all_surveys'),
    path('new/', views.new_surveys, name='new_surveys'),
]

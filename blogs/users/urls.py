from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.index, name='users_index'),
    path('login/', views.login, name='user_login'),
    path('new/', views.new_user, name='new_user'),
    path('allusers/', views.all_users, name='all_users')
]

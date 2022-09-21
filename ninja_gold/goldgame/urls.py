from django.urls import path
from . import views
urlpatterns = [
    path('', views.game),
    path('process_money', views.process_money),
    path('restart', views.restart)
]

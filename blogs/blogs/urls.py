
from django.urls import path, include

urlpatterns = [
    path('surveys/', include('surveys.urls')),
    path('users/', include('users.urls')),
    path('', include('allblogs.urls')),

]

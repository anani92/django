
from django.urls import path, include

urlpatterns = [
    path('', include('login.urls')),
    path('thewall/', include('wallapp.urls')),
]

from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>', views.home),
    path('message', views.write_message),
    path('comment', views.write_comment),
    path('logout', views.logout),

]

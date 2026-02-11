from django.urls import path
from .views import home, create_appointment

urlpatterns = [
    path('', home, name='home'),
    path('new/', create_appointment, name='create_appointment'),
]

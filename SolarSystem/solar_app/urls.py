from django.urls import path
from .views import home, learn, quiz, help

urlpatterns = [
    path('', home, name='home'),
    path('learn/', learn, name='learn'),
    path('quiz/', quiz, name='quiz'),
    path('help/', help, name='help'),
]
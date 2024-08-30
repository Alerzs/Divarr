from django.urls import path
from .views import AllAgahi , OneAgahi , CreatAgahi ,DelateAgahi



urlpatterns = [
    path("oneagahi/<int:pk>" ,OneAgahi.as_view()),
    path("allagahi/" , AllAgahi.as_view()),
    path("creat/" , CreatAgahi.as_view()),
    path("del/<int:pk>" , DelateAgahi.as_view()),
]
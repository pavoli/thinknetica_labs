from django.urls import path
from main.mobile import views

urlpatterns = [
    path('', views.index, name='index'),
]

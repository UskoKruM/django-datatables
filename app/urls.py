from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_programmers/', views.list_programmers, name='list_programmers')
]

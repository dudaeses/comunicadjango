from django.urls import path
from django.http import HttpResponse
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('comentarios/', views.comentarios, name='comentarios'),
]



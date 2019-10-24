from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'product'    

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('add/', views.add, name='add')
]
from django.urls import path
from . import views

app_name = 'association'

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('deletar/<int:id>',views.deletar, name="deletar"),
    path('student/<int:id>', views.student_infos, name="student"),
]
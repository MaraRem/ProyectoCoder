

from django.contrib import admin
from django.urls import path
from AppCoder.views import curso,lista_cursos,inicio,cursos,profesores,estudiantes,entregables

urlpatterns = [
    
    path('agrega_curso/<nombre>/<camada>', curso),
    path('lista_cursos' , lista_cursos),
    path('' , inicio, name='Inicio'),
    path('cursos/' , cursos, name='Cursos'),
    path('profesores/' , profesores, name='Profesores'),
    path('estudiantes/' , estudiantes, name='Estudiantes'),
    path('entregables/' , entregables, name='Entregables'),
]

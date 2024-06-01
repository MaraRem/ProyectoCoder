

from django.contrib import admin
from django.urls import path
from AppCoder.views import (
    curso,
    lista_cursos,
    inicio,
    cursos,
    profesores,
    estudiantes,
    entregables,
    curso_formulario,
    estudiante_formulario,
    entregable_formulario
    )

urlpatterns = [
    
    path('agrega_curso/<nombre>/<camada>', curso),
    path('lista_cursos' , lista_cursos),
    path('' , inicio, name='Inicio'),
    path('cursos/' , cursos, name='Cursos'),
    path('profesores/' , profesores, name='Profesores'),
    path('estudiantes/' , estudiantes, name='Estudiantes'),
    path('entregables/' , entregables, name='Entregables'),
    path('curso-formulario/' , curso_formulario, name='CursoFormulario'),
    path('estudiante-formulario/' , estudiante_formulario, name='EstudianteFormulario'),
    path('entregable-formulario/' , entregable_formulario, name='EntregableFormulario'),
]

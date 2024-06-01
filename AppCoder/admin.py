from django.contrib import admin
from .models import Curso,Profesor,Estudiante,Entregable

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre','camada']
    search_fields = []

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','profesion']
    search_fields = []

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido']
    search_fields = []


# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Entregable)
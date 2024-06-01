from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Estudiante,Entregable
from .forms import CursoFormulario, EstudianteFormulario,EntregableFormulario


# Create your views here.
def curso(req,nombre,camada):
    nuevo_curso= Curso(nombre = nombre, camada = camada)
    nuevo_curso.save()
    return HttpResponse(f""" <p> Curso: {nuevo_curso.nombre} Camada : {nuevo_curso.camada} creado!!! </p>
                        
""")

def lista_cursos(req):

    lista = Curso.objects.all()
    return render(req,"lista_cursos.html", {"lista_cursos" : lista})

def inicio(req):
    return render(req,"inicio.html", {})

def cursos(req):
    return render(req,"cursos.html", {})

def profesores(req):
    return render(req,"profesores.html", {})

def estudiantes(req):
     return render(req,"estudiantes.html", {})

def entregables(req):
     return render(req,"entregables.html", {})



def curso_formulario(req):

    if req.method =='POST':
        
        miformulario = CursoFormulario(req.POST)
        
        
        if miformulario.is_valid():

            data = miformulario.cleaned_data            

            nuevo_curso= Curso(nombre = data['curso'], camada = data['camada'])
            nuevo_curso.save()
        
            return render(req,"inicio.html", {"message": "Curso Creado!!!! "})  
                          
        else:
            return render(req,"inicio.html", {"message": "Tu Curso No pudo ser creado ! "})
        
    else:
        miformulario = CursoFormulario()

        return render(req,"curso_formulario.html", {"miformulario":miformulario})
    


def estudiante_formulario(req):

    if req.method =='POST':
        
        form_estudiante = EstudianteFormulario(req.POST)
        
        
        if form_estudiante.is_valid():

            data_e = form_estudiante.cleaned_data            

            nuevo_e= Estudiante(nombre = data_e['nombre'], apellido = data_e['apellido'])
            
            nuevo_e.save()
        
            return render(req,"inicio.html", {"message": "Estudiante Creado!!!! "})  
                          
        else:
            return render(req,"inicio.html", {"message": "El Estudiante No pudo ser creado ! "})
        
    else:
        form_estudiante = EstudianteFormulario()

        return render(req,"estudiante_formulario.html", {"form_estudiante":form_estudiante})



def entregable_formulario(req):

    if req.method =='POST':
        
        form_entregables = EntregableFormulario(req.POST)
        
        
        if form_entregables.is_valid():

            data_entregable = form_entregables.cleaned_data            

            nuevo_entregable= Entregable(
                nombre = data_entregable['nombre'], 
                fechadeentrega= data_entregable['fechadeentrega'], 
                entregado= data_entregable['entregado']
                )
            
            nuevo_entregable.save()
        
            return render(req,"inicio.html", {"message": "Entregables Registrado OK!!!! "})  
                          
        else:
            return render(req,"inicio.html", {"message": "El Entregable No pudo ser subido ! "})
        
    else:
        form_entregables = EntregableFormulario()

        return render(req,"entregables_formulario.html", {"form_entregables":form_entregables})
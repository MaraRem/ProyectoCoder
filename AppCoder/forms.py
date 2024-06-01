from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()


class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    emal = forms.EmailField()
        

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fechadeentrega = forms.DateField() 
    
    
    
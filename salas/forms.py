from django import forms
from salas.models import Novedad

# la definicion de los formularios utilizando la clase forms 
# que recopila información sobre Salas.

    
class FormularioCrearNovedad(forms.ModelForm):
    class Meta:
        model = Novedad
        fields = ('usuario', 'titulo', 'sala', 'descripcion', 'imagen') 

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 200px;'}), #deberia ser 'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 200px;'}),
            'sala' : forms.Select(attrs={'class': 'form-control','style': 'max-width: 200px;'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control','style': 'max-width: 500px;'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        
class EditarNovedad (forms.ModelForm):
    class Meta:
        model = Novedad
        fields = ('usuario', 'titulo', 'sala', 'descripcion', 'imagen') 
        
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'sala' : forms.Select(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'imagen' : forms.FileInput(attrs={'class': 'form-control-file'}),   
        }


from django import forms
from salas.models import Comentario

# la definicion de los formularios utilizando la clase forms 
# que recopila información sobre Salas.

    
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }
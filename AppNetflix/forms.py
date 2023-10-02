from django import forms
from django.core import validators

class RegistroFormulario(forms.Form):
    usuario = forms.CharField()
    contraseña = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            validators.MinLengthValidator(limit_value=8),
            validators.MaxLengthValidator(
                limit_value=16,
                message='La contraseña debe tener entre 8 y 16 caracteres.'
            ),
        ]
    )
    nombre = forms.CharField()
    apellido = forms.CharField()

class AgregarPeliculaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    genero = forms.CharField(widget=forms.TextInput())
    duracion = forms.CharField(widget=forms.TextInput(), help_text='El formato debe ser HH:MM:SS')
    descripcion = forms.CharField(widget=forms.Textarea())
    imagen = forms.ImageField(help_text='La imagen debe ser un archivo .jpg del tamaño 450x300')
    portada = forms.ImageField(help_text='La portada debe ser un archivo .jpg y preferiblemente del tamaño 1000x1500')

class AgregarSerieForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput())
    genero = forms.CharField(widget=forms.TextInput())
    temporadas = forms.IntegerField(widget=forms.TextInput())
    descripcion = forms.CharField(widget=forms.Textarea())
    imagen = forms.ImageField(help_text='La imagen debe ser un archivo .jpg del tamaño 450x300')
    portada = forms.ImageField(help_text='La portada debe ser un archivo .jpg y preferiblemente del tamaño 1000x1500')

class BuscarForm(forms.Form):
    terminoBusqueda = forms.CharField(label='Buscar', max_length=100, required=False)
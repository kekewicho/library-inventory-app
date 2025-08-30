from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name', 'funado']
        labels = {
            'name': 'Nombre del autor',
            'funado': '¿Autor funado?'
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['title', 'autor', 'stock']
        labels = {
            'title': 'Título del libro',
            'autor': 'Autor',
            'description': 'Descripción',
            'stock': 'Stock disponible'
        }
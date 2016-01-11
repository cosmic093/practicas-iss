from django import forms
from django.forms import ModelForm

class BuscarForm(forms.Form):
    contenido = forms.CharField(max_length=200)

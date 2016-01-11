# -*- coding: utf-8 -*-
from django.forms import ModelForm, extras
from django import forms
from .models import Video

class Modificar(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Modificar, self).__init__(*args, **kwargs)
        self.fields['titulo'].label = 'Título'
        self.fields['descripcion'].label = 'Descripción'
    class Meta:
        model=Video
        exclude=('visitas', 'usuario', 'fecha', 'documento', 'identificador')

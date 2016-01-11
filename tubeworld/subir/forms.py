# -*- coding: utf-8 -*-
from django import forms

class UploadForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    descripcion= forms.CharField(max_length=500)
    tags= forms.CharField(max_length=500)
    privado=forms.BooleanField(initial=False, required=False)
    documento = forms.FileField(
    label='Selecciona un video'
    )

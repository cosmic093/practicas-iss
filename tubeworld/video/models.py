# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Video(models.Model):
    identificador=models.IntegerField()
    titulo=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=500, default='No existe descripción para este video.')
    fecha = models.DateField("Fecha", default=date.today)
    documento = models.FileField(upload_to='.', default='.')
    usuario = models.ForeignKey(User)
    privado=models.BooleanField(default=False)
    visitas=models.IntegerField(default=0)
    def __str__(self):
        return self.titulo

class Tag(models.Model):
    video = models.ForeignKey(Video)
    contenido=models.CharField(max_length=20, default='NULL')
    def __str__(self):
        return self.contenido

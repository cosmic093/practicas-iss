from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Video, Tag
from django.contrib.auth.models import User
import os
from .forms import *

def index(request, video_id):
    video=Video.objects.get(identificador__iexact=video_id)
    video.visitas=video.visitas+1
    video.save()
    tags=Tag.objects.filter(video=video)
    fecha=video.fecha
    #Creamos los videos de interes
    videoList=Video.objects.order_by('-identificador')
    interes=[]
    j=0
    for i in videoList:
        #Para extraer los 10 ultimos videos
        if j<10:
            if i.privado==False or i.usuario == request.user:
                interes.insert(j,i)
                j=j+1

    contexto={"video":video, "tags":tags, "fecha":fecha, "interes":interes, 'user':request.user}
    if video.privado==False or video.usuario == request.user:
        return render(request,"video.html",contexto)
    else:
        return HttpResponseRedirect("/")

def eliminar(request, video_id):
    video=Video.objects.get(identificador__iexact=video_id)
    if video.usuario == request.user:
        dire="tubeworld/media/"+os.path.basename(video.documento.name)
        os.remove(dire)
        video.delete()
    return HttpResponseRedirect("/usuario/perfil")

def modificar(request, video_id):
    video=Video.objects.get(identificador__iexact=video_id)
    if video.usuario == request.user:
        if request.method == 'POST':
            form = Modificar(request.POST ,request.FILES, instance=video)
            if form.is_valid():
                video.save()
                return redirect("/usuario/perfil")
        else:
            form = Modificar(instance=video)
        return render(request, 'modificar.html', {'form': form, 'user':request.user})
    else:
        return redirect("/usuario/perfil")

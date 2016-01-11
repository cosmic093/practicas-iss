from django.shortcuts import render
from django.http import HttpResponse
from video.models import Video, Tag
from .forms import BuscarForm
from django.contrib.auth.models import User

def buscar(request,campo):
	tags=Tag.objects.filter(contenido__contains=campo)
	videos=Video.objects.filter(titulo__contains=campo)
	encontrado=[]
	j=0
	for i in tags:
		if j<24:
			if i.video.privado==False or i.video.usuario == request.user:
				encontrado.insert(j,i.video)
				j=j+1
	for i in videos:
		if j<24:
			if i.privado==False or i.usuario == request.user:
				encontrado.insert(j,i)
				j=j+1
	return encontrado

def index(request):
	if request.method == 'POST':
		form = BuscarForm(request.POST)
		if form.is_valid():
			contenido = request.POST['contenido']
			encontrado=buscar(request,contenido)
			return render(request, "buscar.html", {'contenido':contenido, 'encontrado':encontrado, 'user': request.user})
	else:
		form = BuscarForm()

	videoList=Video.objects.order_by('-identificador')
	videos=[]
	j=0
	for i in videoList:
		#Para extraer los 8 ultimos videos
		if j<8:
			if i.privado==False or i.usuario == request.user:
				videos.insert(j,i)
				j=j+1
	contexto={"videos":videos, 'form': form, 'user': request.user}
	return render(request,"index.html",contexto)

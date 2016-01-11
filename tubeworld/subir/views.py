from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from subir.forms import UploadForm
from video.models import Video, Tag

@login_required()
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST ,request.FILES)
        video = Video.objects.all()
        if form.is_valid():
            num=0
            for i in video:
                if i.identificador>num:
                    num=i.identificador
            num=num+1
            newdoc = Video(identificador=num, titulo = request.POST['titulo'],descripcion = request.POST['descripcion'],privado=request.POST.get('privado', False),documento = request.FILES['documento'], usuario=request.user)
            newdoc.save(form)
            v=[]
            var=request.POST['tags']
            aux=""
            j=0
            for i in var:
                 if i==',':
                         v.insert(j,aux)
                         aux=""
                         j=j+1
                 else:
                         aux=aux+i
            v.insert(j,aux)
            for i in v:
                newTag=Tag(video=newdoc, contenido=i)
                newTag.save()
            return redirect("uploads")
    else:
        form = UploadForm()
        video = Video.objects.all()
    return render(request, 'upload.html', {'form': form, 'user':request.user})

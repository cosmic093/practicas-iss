from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from video.models import Video

from forms import SignUpForm

@login_required()
def perfil(request):
    videoList=Video.objects.filter(usuario=request.user)
    videos=[]
    j=0
    for i in videoList:
        videos.insert(j,i)
        j=j+1
    return render_to_response('perfil.html', {'user': request.user, 'videos':videos}, context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name

            user.save()
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()

    data = {
        'form': form, 'user':request.user
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))

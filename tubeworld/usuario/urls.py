from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^registro$', 'usuario.views.signup', name='signup'),
    url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
    url(r'^logout$', logout, {'template_name': 'logout.html', }, name="logout"),
    url(r'^perfil$', 'usuario.views.perfil', name='perfil'),
]

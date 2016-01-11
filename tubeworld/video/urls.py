from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<video_id>[0-9]+)/$', views.index, name='index'),
    url(r'^eliminar/(?P<video_id>[0-9]+)/$', views.eliminar, name='eliminar'),
    url(r'^modificar/(?P<video_id>[0-9]+)/$', views.modificar, name='modificar'),    
]

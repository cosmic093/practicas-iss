from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^uploads/', 'subir.views.upload_file', name="uploads"),
    url(r'^video/', include('video.urls')),
    url(r'^usuario/', include('usuario.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('main.urls'), name="main"),
)+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

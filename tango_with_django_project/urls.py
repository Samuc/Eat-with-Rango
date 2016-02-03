"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import patterns, url, include
from rango import views
from django.conf import settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about$', views.about, name='about'),
    url(r'^highchart$', views.highchart, name='highchart'),
    url(r'^reclama_bares/$', views.reclama_bares, name='reclama_bares'),
    url(r'^reclama_visitas/$', views.reclama_visitas, name='reclama_visitas'),
    url(r'^rango/', include('rango.urls')),
    url(r'^base/', views.base, name='base'), # o     url(r'^$', include('rango.urls')),
    url(r'^$', views.index, name='index'), # o     url(r'^$', include('rango.urls')),
]

from django.conf import settings # New Import
from django.conf.urls.static import static # New Import


if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

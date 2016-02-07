from django.contrib import admin
from django.conf.urls import patterns, url, include
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^highchart/$', views.highchart, name='highchart'),
    url(r'^admin/', admin.site.urls),
    url(r'^bar/(?P<bar_name_url>[\w\-]+)/$', views.bar, name='bar'),
    url(r'^bar/(?P<bar_name_url>[\w\-]+)/add_tapa/$', views.add_tapa, name='add_tapa'),
    url(r'^add_bar/$', views.add_bar, name='add_bar'), # NEW MAPPING!
    url(r'^add_tapa/$', views.add_tapa_save, name='add_tapa_save'), # NEW MAPPING!
#    url(r'^tapa/$', views.tapa, name='tapa'), # NEW MAPPING!
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^reclama_bares/$', views.reclama_bares, name='reclama_bares'),
    url(r'^reclama_visitas/$', views.reclama_visitas, name='reclama_visitas'),
    url(r'^voto_tapa/$', views.voto_tapa, name='voto_tapa'),

 ]

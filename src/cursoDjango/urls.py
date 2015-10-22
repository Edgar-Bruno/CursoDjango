"""cursoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^aula3/$', 'aula3.views.index', name='aula3_index'),
	url(r'^aula3/(?P<id>\d+)/$', 'aula3.views.detail', name='aula3_detail'),

    url(r'^aula4/$', 'aula4.views.index', name='aula4_index'),

    url(r'^aula6/$', 'aula6.views.index', name='aula6_index'),
    url(r'^aula6/(?P<id>\d+)/$', 'aula6.views.detail', name='aula6_detail'),

    url(r'^aula6/(?P<nome>[-\w]+)/$', 'aula6.views.exemplo'),

    url(r'^nave/$', 'aula_formset.views.submit_nave', name='nave'),


    #url(r'^nave/$', 'aula_formset.views.submit_nave', {'formset_class': 'eDGAR bRUNO'}, name='nave'),
    # url(r'^stacked/$', 'formset', {'formset_class': ContactFormset, 'template': 'example/formset-stacked.html'}, name='example_stacked'),
    url(r'^admin/', include(admin.site.urls)),
]

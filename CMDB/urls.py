#coding:utf-8
"""CMDB URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', views.index),
    url(r'^signin/', views.signin),
    url(r'^signup/', views.signup),
    url(r'^serverRegister/',views.serverRegister),

]
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^login/$',include('login.urls'))
# ]
# urlpatterns += staticfiles_urlpatterns()

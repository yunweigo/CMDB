from django.conf.urls import include, url
from .views import *
urlpatterns = [
    url(r'index/', index),
    url(r'signin/',signin),
    url(r'signup/',signup),

]
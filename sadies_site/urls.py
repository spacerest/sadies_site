from django.conf.urls import url
from django.contrib import admin
from website.views import * 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^(?P<nav>\w{0,20})/$', findpage)
]

from django.conf.urls import url
from django.contrib import admin
from website.views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^(?P<nav>\w{0,20})/$', findpage)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings

from django_hosts import patterns, host

from django.conf.urls import handler404, handler500

from . import views


host_patterns = patterns(
    '',
    host(r'www', settings.ROOT_URLCONF, name="www"),
    host(r'blog', 'blog.urls', name="blog"),

)

# MANEJO DE ERRORES HTTP
handler404 = views.Error404 # Error 404
handler500 = views.Error500 # Error 500

from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.slamitsaas import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slamit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('apps.slamitsaas.urls')),
)

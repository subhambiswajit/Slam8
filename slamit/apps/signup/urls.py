from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slamit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^$', TemplateView.as_view(template_name='login/index.html')),
    
)

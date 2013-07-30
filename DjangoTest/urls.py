from django.conf.urls import patterns, include, url

from django.contrib import admin
from DjangoTest.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^now/$', current_datetime),
    url(r'^now/plus\d{1,2}hours/$', hours_ahead),
)

# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('cms.urls')),

)

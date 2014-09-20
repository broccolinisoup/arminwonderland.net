#! /usr/bin/env python2.7
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.views import serve
from django.contrib import admin
from aydoganersoz.home.views import *

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^blogpost/$', BlogPostView.as_view(), name='blogpost'),
    url(r'^aboutme/$', AboutMeView.as_view(), name='aboutme'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
	#url(r'^blog/(?P<id>\d+)/$', BlogView.as_view(), name='blog'),

	
	(r'^tinymce/', include('tinymce.urls')),
	# static
	url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve,
		{'show_indexes': True, 'insecure': False}),
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),

	#TO DO: Admin tools'u ayaga kaldir.
	#url(r'^admin_tools/', include('admin_tools.urls')),
)

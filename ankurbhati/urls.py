from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
	#url(r'^$', 'home.views.index', name='index'),
	url(r'^$', 'home.views.blogs', name='index'),
	url(r'^contact/$', 'home.views.contact', name='contact'),
    url(r'^about/$', 'home.views.about', name='about'),
    url(r'^projects/$', 'home.views.projects', name='projects'),
    url(r'^blogs/$', 'home.views.blogs', name='blogs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^blogs/(?P<category>\d+)/$', 'home.views.blogs', name='blogs'),
    url(r'^blogs/(?P<category>\d+)/(?P<blog>\d+)/$', 'home.views.blogs', name='blogs'),
    url(r'^blogs/(?P<search_text>\w+)/$', 'home.views.blogs', name='blogs'),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

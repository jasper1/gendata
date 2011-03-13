from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datagen.views.home', name='home'),
    # url(r'^datagen/', include('datagen.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Serve static files for debug mode
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^images?/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.IMAGE_ROOT}),
        (r'^css/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.CSS_ROOT}),
        (r'^js?/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.JS_ROOT}),                        
    )
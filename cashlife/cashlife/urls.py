from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^categories/', include('categories.urls')),
                       url(r'^docs/', include('rest_framework_swagger.urls')),
                       )
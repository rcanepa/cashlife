from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryList, CategoryDetail


categories_url = patterns('',
                          url(r'^$', CategoryList.as_view(), name='categories-list'),
                          url(r'^(?P<pk>[0-9]+)/$', CategoryDetail.as_view(), name="categories-detail"),
                          )

urlpatterns = patterns('',
                       url(r'^', include(categories_url)),
                       )
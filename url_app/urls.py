from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^api/$', views.api_list, name='api_list'),
    url(r'^api/detail/$', views.api_detail, name='api_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shortner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'', include('url_app.urls')),
)
#project urls sportsproject/urls.py
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportsproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url (r'^$', 'roster.views.home'),
    url (r'^', include('roster.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

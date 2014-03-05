#app urls roster/urls.py
from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    url(r'^team/(?P<pk>\d+)$', views.team, name='roster_team'),
    #url(r'^team$', views.team, name='roster_team'),
    url(r'^team/player/(?P<pk>\d+)$', views.player, name='roster_player'),
    #url(r'^team/$', views.teamList, name='roster_team_list'),
    #url(r'^player/$', views.playerList, name='roster_player_list'),
    #url(r'^team/(?P<pk>\d+)$', views.team, name='roster_team'),
    #url(r'^player/(?P<pk>\d+)$', views.player, name='roster_player'),
    )
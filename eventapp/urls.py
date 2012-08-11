""" URLs for eventapp"""
from django.conf.urls import patterns, url

urlpatterns = patterns('',
     url(r'^$', 'eventapp.views.index', name='index'),
     url(r'^login$', 'django.contrib.auth.views.login',
         {'template_name': 'login.html'}, name="login"),
     url(r'^logout$', 'eventapp.views.logout', name="logout"),
     url(r'^like', 'eventapp.views.like', name="like"),
     url(r'^subscribe', 'eventapp.views.subscribe', name="subscribe")
)

from django.conf.urls import patterns, url
from quadratic import views

urlpatterns = patterns('',
    url(r'^$', views.index_eq),
    url(r'^results/$', views.results),
)
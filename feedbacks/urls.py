from django.conf.urls import patterns, url
from feedbacks import views

urlpatterns = patterns('',
    url(r'^$', views.FeedbackView.as_view(), name='feedback'),
)
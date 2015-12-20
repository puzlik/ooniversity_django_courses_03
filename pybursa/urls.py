from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from pybursa import views
from feedbacks.views import FeedbackView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),  
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls'), name='results'),
    url(r'^feedback/', FeedbackView.as_view(), name='feedback'),
)

handler404 = 'pybursa.views.page_not_found'
handler500 = 'pybursa.views.internal_error'
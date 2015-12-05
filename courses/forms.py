# -*- coding: utf-8 -*-
from django.forms import ModelForm
from courses.models import Course, Lesson
from django import forms

class CourseModelForm(ModelForm):
    class Meta:
    	model = Course
    	fields = ['name', 'short_description', 'description', 'coach', 'assistant']

class LessonModelForm(ModelForm):
    class Meta:
    	model = Lesson
    	fields = ['subject', 'description', 'course', 'order']
    	localized_fields = ('course',)

# -*- coding: utf-8 -*-
from django.forms import ModelForm
from students.models import Student
#from courses.models import Course
from django import forms

class StudentModelForm(ModelForm):
    class Meta:
    	model = Student
    	fields = ['name', 'surname', 'date_of_birth', 'email', 'phone', 'address', 'skype', 'courses']

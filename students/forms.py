# -*- coding: utf-8 -*-
from django.forms import ModelForm
from students.models import Student

class StudentModelForm(ModelForm):
    class Meta:
    	model = Student
    	fields = '__all__'
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms

class QuadraticForm(forms.Form):
    a = forms.IntegerField(label="коэффициент a:", widget=forms.TextInput)
    b = forms.IntegerField(label="коэффициент b:", widget=forms.TextInput)
    c = forms.IntegerField(label="коэффициент c:", widget=forms.TextInput)

    def clean_a(self):
    	data = self.cleaned_data['a']
    	if data == 0:
    		raise forms.ValidationError("коэффициент при первом слагаемом уравнения не может быть равным нулю")
    	return data

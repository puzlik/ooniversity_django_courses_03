# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()
    c = forms.FloatField()
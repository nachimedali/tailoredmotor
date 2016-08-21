from __future__ import unicode_literals
from django import forms
from django.db import models

# Create your models here.

class updat(forms.Form):
	Dm = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control c-square c-theme','ng-model':'Dma','ng-min':'25', 'ng-max':'100','placeholder' : 'Motor Diamater'}))
	Lm = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control c-square c-theme','ng-model':'Lma', 'placeholder' : 'Motor Length '}))
	Ds = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control c-square c-theme','ng-model':'Dsa','placeholder' : 'Shaft Diamater'}))
	Dt = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control c-square c-theme','ng-model':'Dta', 'placeholder' : 'Diamater Thread'}))
	Dc = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control c-square c-theme','ng-model':'Dca', 'placeholder' : 'Centering Diamater '}))
	Dp = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control c-square c-theme','ng-model':'Dpa', 'placeholder' : 'Pitch Diamater'}))
	Ls = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control c-square c-theme','ng-model':'Lsa','placeholder' : 'Length Shaft'}))

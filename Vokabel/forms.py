from django import forms

from .models import *

class NounForm(forms.ModelForm):
	class Meta:
		model=Noun
		fields="__all__"

class VerbForm(forms.ModelForm):
	class Meta:
		model=Verb
		fields="__all__"

class AdjectiveForm(forms.ModelForm):
	class Meta:
		model=Adjective
		fields="__all__"

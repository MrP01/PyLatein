from django import forms

from Vokabel.models import VocGroup

class VocSelectForm(forms.Form):
    vocgroups=forms.ModelMultipleChoiceField(VocGroup.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={"class": "selectpicker", "data-live-search": "true"}))


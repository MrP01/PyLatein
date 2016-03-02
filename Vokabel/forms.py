from django import forms

from .models import *

class AbstractVocForm(forms.ModelForm):
    class Meta:
        fields="__all__"

    vocgroups=forms.ModelMultipleChoiceField(VocGroup.objects.all(),
        widget=forms.widgets.SelectMultiple(attrs={"class": "selectpicker", "data-live-search": "true"}))

    def __init__(self, *args, **kwargs):
        if kwargs.get("instance"):
            initial = kwargs.setdefault("initial", {})
            initial["vocgroups"] = [t.pk for t in kwargs["instance"].vocgroup_set.all()]
        super(AbstractVocForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AbstractVocForm, self).save(False)
        old_save_m2m = self.save_m2m
        def save_m2m():
           old_save_m2m()
           instance.vocgroup_set.clear()
           for group in self.cleaned_data["vocgroups"]:
               instance.vocgroup_set.add(group)
        self.save_m2m = save_m2m
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class NounForm(AbstractVocForm):
    class Meta(AbstractVocForm.Meta):
        model=Noun

class VerbForm(AbstractVocForm):
    class Meta(AbstractVocForm.Meta):
        model=Verb

class AdjectiveForm(AbstractVocForm):
    class Meta(AbstractVocForm.Meta):
        model=Adjective

class VocGroupForm(forms.ModelForm):
    class Meta:
        model=VocGroup
        fields="__all__"

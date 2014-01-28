from django import forms

import autocomplete_light

from .models import TestMtm, TestFk, TestOto


class TestFkModelForm(forms.ModelForm):
    relation = autocomplete_light.ModelChoiceField('RelatedModelAutocomplete')

    class Meta:
        model = TestFk


class TestOtoModelForm(forms.ModelForm):
    relation = autocomplete_light.ModelChoiceField('RelatedModelAutocomplete')

    class Meta:
        model = TestOto


class TestMtmModelForm(forms.ModelForm):
    relation = autocomplete_light.ModelMultipleChoiceField('RelatedModelAutocomplete')

    class Meta:
        model = TestMtm

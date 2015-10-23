from django import forms
from django.forms import fields, models, formsets, widgets
from aula_formset.models import Nave, Ficha_t


class NaveForms(forms.ModelForm):
	class Meta:
		model = Nave
		fields = ['nave']

class Ficha_tForms(forms.ModelForm):
    class Meta:
        model = Ficha_t
        fields = ['caracteristica', 'informacao', 'radio']
        exclude = ('nave',)

    CHOICES = (('1', 'Um',), ('2', 'Dois',))
    radio = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,
    						help_text = ("Enter the same password as above, for verification."))

Ficha_tFormset = formsets.formset_factory(Ficha_tForms)
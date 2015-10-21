from django import forms
from aula_formset.models import Nave, Ficha_t


class NaveForms(forms.ModelForm):
	class Meta:
		model = Nave
		fields = ['nave']

class Ficha_tForms(forms.ModelForm):
    class Meta:
        model = Ficha_t
        fields = ['caracteristica', 'informacao']
        exclude = ('nave',)
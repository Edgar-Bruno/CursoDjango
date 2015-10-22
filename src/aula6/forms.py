# -*- coding: utf-8 -*-

from django import forms
from aula6.models import Contato


class ContatoForms(forms.Form):

	Nome = forms.CharField(label=u'Nome', max_length=100)
	Sobrenome = forms.CharField(label=u'Sobrenome', max_length=30)
	Email = forms.EmailField(label=u'E-mail', max_length=100)
	Twitter = forms.URLField(label='Twitter', max_length=100)
	Datanascimento = forms.DateField(label=u'Data de nascimento', input_formats=['%Y-%m-%d'])
	#   """Image upload form."""
	#image = forms.ImageField()

	def saveContato(self, Contato=None):

		if Contato:

			Contato.nome = self.cleaned_data.get('Nome')
			Contato.sobrenome = self.cleaned_data.get('Sobrenome')
			Contato.email = self.cleaned_data.get('Email')
			Contato.twitter = self.cleaned_data.get('Twitter')
			Contato.Datanascimento = self.cleaned_data.get('Datanascimento')
			#m.model_pic = form.cleaned_data('image')

			#print Contato.imagez

			Contato.save()
			return Contato

		else:
			print 'else form aula6'

			objForms = Contato(
				nome = self.cleaned_data.get('Nome'),
				sobrenome = self.cleaned_data.get('Sobrenome'),
				email = self.cleaned_data.get('Email'),
				twitter = self.cleaned_data.get('Twitter'),
				datanascimento = self.cleaned_data.get('Datanascimento')
			)

			objForms.save()

			return objForms

	# validar para entrar uma única ocorrencia dessa ocorrencia do campo
	# clean_Campo = Retorna o erro aonde o campo eesta

	#clean = Retorna qualquer marcado

	def clean_Email(self):
		Email = self.cleaned_data.get('Email')
		#Contato.objects.filter(campoModel=Email):
		if Contato.objects.filter(email=Email):
			raise forms.ValidationError(u'Esse emails já [ %s ]foi cadastrado' % Email)
		return Email
	
	def clean_Twitter(self):
		Twitter = self.cleaned_data.get('Twitter')
		#Contato.objects.filter(campoModel=Email):
		if Contato.objects.filter(twitter=Twitter):
			raise forms.ValidationError(u'Esse emails já [ %s ]foi cadastrado' % Twitter)
		return Twitter
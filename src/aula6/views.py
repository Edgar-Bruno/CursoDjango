# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404


from aula6.models import Contato
from aula6.forms import ContatoForms


def index(request):
	
	contatos = Contato.objects.all()

	if request.method == 'POST':

		novoForms = ContatoForms(request.POST)
		
		if novoForms.is_valid():

			novoForms.saveContato()

			return HttpResponseRedirect(reverse('aula6_index'))
	else:

		novoForms = ContatoForms()

	return render(request, 'index.html',
		{
		'vAux': contatos,
		'Formulario': novoForms
		}
		)

def detail(request, id):

	checkContato = get_object_or_404(Contato, id=id)

	Initial = {'Nome': checkContato.nome,
			'Sobrenome': checkContato.sobrenome,
			'Email': checkContato.email,
			'Twitter': checkContato.twitter,
			'Datanascimento': checkContato.datanascimento
			}

	if request.method == 'POST':

		editForms = ContatoForms(request.POST)
		
		if editForms.is_valid():

			editForms.saveContato(Contato=checkContato)

			return HttpResponseRedirect(reverse('aula6_index'))
	else:
		editForms = ContatoForms(initial=Initial)
	return render(request, 'detail.html',
		{
		'contaEDIT': checkContato,
		'Formulario': editForms
		}
		)


def exemplo(request, nome='unknown'):

	retorno =  Contato.objects.filter(nome = nome)
	print retorno
	return render(request, 'exemplo.html',{ 'RE' : retorno})
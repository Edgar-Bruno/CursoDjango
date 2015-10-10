# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from aula6.models import Contato

def index(request):

	contatos = Contato.objects.all()

	if request.method == 'POST':
		#nome = request.POST.get('Nome')
		#sobrenome = request.POST.get('Sobrenome')
		#email = request.POST.get('Email')
		#twitter = request.POST.get('Twitter')
		#datanascimento = request.POST.get('DataNace')
		
		novoContato = Contato(
			nome = request.POST.get('Nome'),
			sobrenome = request.POST.get('Sobrenome'),
			email = request.POST.get('Email'),
			twitter = request.POST.get('Twitter'),
			datanascimento = request.POST.get('DataNace')
		)

		novoContato.save()

		return HttpResponseRedirect(reverse('aula6_index'))

	else:
		nome = ''
		sobrenome = ''
		email =''
		twitter = ''

		return render(request, 'index.html', {'vAux': contatos})

	"""return render(request, 'index.html',
		{'nome':nome,
		'sobrenome': sobrenome,
		'email': email,
		'twitter': twitter}"""
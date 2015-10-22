# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.method == 'POST':
		nome = request.POST.get('name', u'Não tem nome')
		return HttpResponse(u'O nome é %s' % nome)
	else:
		formulario = '''
		<form action="." method="post">
		<input type="text" name="name" maxlength="100"/>
		<button type="submit">Enviar</button>
		</form>
		'''
		return HttpResponse(formulario)

def detail(request, id):
	return HttpResponse(u'O Id é: %s' % id)



"""
# Metodo GET
def index(request):
	nome = request.GET.get('nome', u'Não tem nome')
	return HttpResponse(u'O nome é %s' % nome)


def index(request):
	method = request.method
	return HttpResponse(u'O método é %s' % method)


def index(request):
	response = HttpResponse()
	response.write(u'<h1>Olá mundo</h1>')
	return response

"""
# Create your views here.

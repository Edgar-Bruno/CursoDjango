from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import forms

from django.shortcuts import render_to_response
from django.forms.formsets import formset_factory

from .forms import NaveForms, Ficha_tForms, Ficha_tFormset
from .models import Ficha_t


#def submit_nave(request, formset_class):
#print '----->>>', formset_class
def submit_nave(request):

    #Ficha_tFormSet = formset_factory(Ficha_tForms, extra=5)

    if request.method == "POST":

    	objForm = NaveForms(request.POST or None)
    	formset = Ficha_tFormset(request.POST)

        print '------', formset

    	if objForm.is_valid():
    		msn = "Ok"

    		instance = objForm.save(commit=False)
    		instance.save()

    		for formX in formset.forms:
    			formUP = formX.save(commit=False)
    			formUP.nave_id = instance.id
    			formUP.save()

    	else:

    		msn = "Algo saiu errado"

    	return render_to_response('indexX.html',
    		{'msn'			: msn},
    		context_instance=RequestContext(request))
    else:
    	print 'else'
    	return render_to_response('indexX.html',
    		{'formA'		: NaveForms(),
    		 'formset' 	: Ficha_tFormset()},
    		context_instance=RequestContext(request))
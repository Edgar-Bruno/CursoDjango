# -*- coding: utf-8 -*-

from django.db import models

class Contato(models.Model):

	nome = models.CharField(max_length=100, blank=True)
	sobrenome = models.CharField(max_length=30)
	email = models.EmailField(max_length=100)
	twitter = models.URLField(max_length=100)
	datanascimento = models.DateField()
	#model_pic = models.ImageField(upload_to = '/home/edgarbruno/Imagens/Gifs/', default = '/home/edgarbruno/Imagens/coringa louco comic 2.png')

	def __unicode__(self):
		return unicode(self.nome)


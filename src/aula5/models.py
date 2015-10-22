# -*- coding: utf-8 -*-

from django.db import models

class contato(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    twitter = models.URLField()
    datanascimento = models.DateField()

    def __unicode__(self):
        return unicode(self.nome)


    	



# Create your models here.

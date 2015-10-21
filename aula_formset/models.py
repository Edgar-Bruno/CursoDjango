from django.db import models

# Create your models here.
class Nave(models.Model):
    pub_date = models.DateTimeField('Date Published', auto_now_add = True)
    nave = models.CharField(max_length=20, blank=True, null=True)

class Ficha_t(models.Model):
    nave = models.ForeignKey(Nave)
    caracteristica = models.CharField(max_length=40, blank=True, null=True)
    informacao = models.CharField(max_length=140, blank=True, null=True)
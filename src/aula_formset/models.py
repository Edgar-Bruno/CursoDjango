from django.db import models

# Create your models here.
class Nave(models.Model):
    pub_date = models.DateTimeField('Date Published', auto_now_add = True)
    nave = models.CharField(max_length=20, blank=True, null=True)

class Ficha_t(models.Model):
	PRIORITY = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'))

	nave = models.ForeignKey(Nave)
	caracteristica = models.CharField(choices=PRIORITY, default=0, max_length=20,)
	informacao = models.CharField(max_length=140, blank=True, null=True)
	radio = models.CharField(max_length=2, blank=False, null=True)
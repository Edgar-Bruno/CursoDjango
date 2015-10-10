from django.db import models

class Pessoa(models.Model):
	nome = models.CharField(max_length = 40)
	telefone = models.CharField(max_length = 11)
	endereco = models.TextField()
	"""docstring for ClassName
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg


# Create your models here.
"""
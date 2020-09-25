from django.db import models
from django.utils import timezone

class Publicar(models.Model):
	autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	data_criar = models.DateTimeField(
		default=timezone.now)
	data_publicar = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.data_publicar = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

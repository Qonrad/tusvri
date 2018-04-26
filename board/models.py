from django.db import models
from django.urls import reverse

# Create your models here.

class Position(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	pub_date = models.DateTimeField('date published')
	time_commitment = models.IntegerField(default=0)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('position-detail', args=[str(self.id)])



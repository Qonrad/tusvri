from django.db import models

# Create your models here.

class Position(models.Model):
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    time_commitment = models.IntegerField(default=0)
    investigator = models.CharField(max_length=100)




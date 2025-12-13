from django.db import models

from django.db import models

class measurements(models.Model):
  date=models.DateTimeField()
  ammonia = models.FloatField()
  nitrites = models.FloatField()

# Create your models here.

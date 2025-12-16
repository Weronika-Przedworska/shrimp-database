from django.db import models

class Tank(models.Model):
    size_liters = models.IntegerField() # volume of aquarium
    brand = models.CharField(max_length=100) # aquarium brand name
    water_type = models.CharField(max_length=50) #freshwater or saltwater or some secret third thing
    def __str__(self):
        return f"{self.brand} ({self.size_liters} liters)"


class Measurement(models.Model):
  date=models.DateTimeField(auto_now_add=True) #automatically gets date, better for accuracy
  ammonia = models.FloatField() # in parts per million (ppm)
  nitrites = models.FloatField() # in ppm 
  nitrates=models.FloatField() # in ppm 
  tank=models.ForeignKey(Tank, on_delete=models.CASCADE, related_name="measurements")

  def __str__(self):
        return f"{self.tank.brand} at ({self.date})"



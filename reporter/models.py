from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Incidence(models.Model):
    name=models.CharField(max_length=20)
    location=models.PointField(srid=4326)

    def __str__(self):
        return self.name
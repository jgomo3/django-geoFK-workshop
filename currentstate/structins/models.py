from django.contrib.gis.db import models


class Inspection(models.Model):
  time = models.DateTimeField()
  observations = models.TextField()
  structure = models.ForeignKey("Structure")


class Structure(models.Model):
  name = models.CharField(max_length=100)
  feature = models.PolygonField()
  objects = models.GeoManager()

  def __unicode__(self):
      return self.name

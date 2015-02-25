from django.db import models

class Individual(models.Model):
  name = models.CharField(max_length=100)
  belogns_to = models.ForeignKey('Group')

  def __unicode__(self):
      return self.name

class Group(models.Model):
  name = models.CharField(max_length=100)

  def __unicode__(self):
      return self.name

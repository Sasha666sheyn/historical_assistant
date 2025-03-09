from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class War(models.Model):
    title = models.TextField(blank = True)
    description = models.TextField(blank = True)
    embedding = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.description



class Tatneft(models.Model):
    title = models.TextField(blank = True)
    description = models.TextField(blank = True)
    embedding = ArrayField(models.FloatField(), size=768, null=True, blank=True)
    def __str__(self):
        return self.title
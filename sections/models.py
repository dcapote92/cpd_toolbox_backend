from django.db import models

class Section(models.Model):
    name = models.CharField(null=False, blank=False)

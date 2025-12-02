from django.db import models

class Model(models.Model):
    name = models.CharField(null=False, blank=False)

    def __str__(self):
        return self.name

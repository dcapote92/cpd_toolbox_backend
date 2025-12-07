from django.db import models
from models.models import Model
from sections.models import Section
from django.conf import settings


class Scale(models.Model):
    number = models.IntegerField()
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name='scales')
    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name='scales')
    weight = models.IntegerField()
    measurement_date = models.DateField()
    measured_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='measured_scales')
    calibration_date = models.DateField()
    calibrated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='calibrated_scales')
    clean_date = models.DateField()
    cleaned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='cleaned_scales')

    def __str__(self):
        return self.number

from django.contrib import admin
from scales.models import Scale

@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'weight', 'measurement_date', 'calibration_date', 'clean_date')

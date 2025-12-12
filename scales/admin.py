from django.contrib import admin
from scales.models import Scale


@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'model',
        'weight',
        'measurement_date',
        'measured_by',
        'calibration_date',
        'calibrated_by',
        'clean_date',
        'cleaned_by'
    )

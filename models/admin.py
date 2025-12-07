from django.contrib import admin
from models.models import Model


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

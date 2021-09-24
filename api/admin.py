from django.contrib import admin

from api import models


@admin.register(models.VIN)
class VINAdmin(admin.ModelAdmin):
    list_display = [
        'vin_code',
        'make',
        'model',
        'year',
        'manufacturer',
        'engine',
        'trim',
        'transmission'
    ]
    search_fields = [
        'vin_code',
        'make',
        'model',
        'manufacturer'
    ]
    list_filter = [
        'make',
        'manufacturer',
        'year'
    ]

from django.contrib import admin
from .models import Carrier

class CarrierAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['carrier_company']
    list_display = ['carrier_company', 'carrier_id', 'carrier_vehicle', 'carrier_tel',
                    'carrier_status']
    #list_display_links = ['carrier_company']
    list_editable = ['carrier_vehicle', 'carrier_tel',
                    'carrier_status']

admin.site.register(Carrier, CarrierAdmin)


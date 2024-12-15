from django.contrib import admin

from .models import Supplier, Category

class SupplierAdmin(admin.ModelAdmin):
    search_fields = ['supplier_company']
    list_per_page = 10
    list_display = ['supplier_id', 'supplier_company', 'supplier_name',
                    'supplier_job','supplier_address','supplier_city','supplier_area',
                    'supplier_postalcode','supplier_country','supplier_tel','supplier_fax',
                    'supplier_status','supplier_homepage']
    #list_display_links = ['supplier_company']
    list_editable = ['supplier_company', 'supplier_name',
                    'supplier_job','supplier_address','supplier_city','supplier_area',
                    'supplier_postalcode','supplier_country','supplier_tel','supplier_fax',
                    'supplier_status','supplier_homepage']

class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['category_name']
    list_display = ['category_id','category_name', 'category_notes', 'category_inittime', 'category_updatetime','category_photo']
    #list_display_links = ['category_name']
    list_editable = ['category_name', 'category_notes', 'category_inittime', 'category_updatetime','category_photo']

admin.site.register(Supplier, SupplierAdmin)

admin.site.register(Category, CategoryAdmin)



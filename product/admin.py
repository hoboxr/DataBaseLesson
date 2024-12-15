from django.contrib import admin
from .models import Product, Information, Order, OrderDetail


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['product_id']
    list_display = ['product_id', 'category', 'product_name', 'product_quantity',
                    'product_price', 'product_inventory', 'product_orderquantity',
                    'product_reorderquanatity', 'product_detail', 'product_status','product_photo']
    list_editable = ['product_name', 'product_quantity',
                     'product_price', 'product_inventory', 'product_orderquantity',
                     'product_reorderquanatity', 'product_detail', 'product_status','product_photo']


class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['order_C_name']
    list_display = ['order_id', 'order_customer_id', 'order_carrier_id', 'order_orderdate', 'order_senddate',
                    'order_receivedate', 'order_confirmdate', 'order_price', 'order_charge', 'order_C_name',
                    'order_C_Address',
                    'order_C_City', 'order_C_Area', 'order_C_PostalCode', 'order_C_Country',
                    'order_Payway', 'order_Insurance']
    list_editable = ['order_carrier_id', 'order_orderdate', 'order_senddate',
                     'order_receivedate', 'order_confirmdate', 'order_price', 'order_charge', 'order_C_name',
                     'order_C_Address',
                     'order_C_City', 'order_C_Area', 'order_C_PostalCode', 'order_C_Country',
                     'order_Payway', 'order_Insurance']


class InformationAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['info_productbarch_id', 'info_product_id', 'info_productiondate', 'info_expirationdate']
    list_editable = ['info_productiondate', 'info_expirationdate']


class OrderDetailAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['od_id', 'od_product_id', 'od_weight', 'od_quantity', 'od_notes']
    list_editable = ['od_weight', 'od_quantity', 'od_notes']


admin.site.register(Product, ProductAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)

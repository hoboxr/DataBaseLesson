from django.contrib import admin

from .models import Customer, Address


# 在admin中注册绑定
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['customer_id']
    list_display = ['customer_id', 'customer_name', 'customer_tel', 'customer_status',
                    'customer_password','address']
    #list_display_links = ['custoner_name']
    list_editable =  ['customer_name', 'customer_tel', 'customer_status',
                    'customer_password','address',]

class AddressAdmin(admin.ModelAdmin):
    search_fields = ['address_id']
    list_per_page = 10
    list_display = ['address_id', 'customer_address', 'customer_company', 'customer_job', 'customer_city','customer_area',
                    'customer_postalcode','customer_fax','customer_country']
    #list_display_links = ['customer_address']
    list_editable = ['customer_address', 'customer_company', 'customer_job', 'customer_city','customer_area',
                    'customer_postalcode','customer_fax','customer_country']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)

#admin.site.site_header：这个属性会改变管理站点的页面头部文本，
# 也就是你在 Django admin 管理页面最上方看到的标题。
admin.site.site_header = '后台管理系统'

#admin.site.site_title：这个属性会改变管理站点的 <title> 元素的文本，
# 也就是你在浏览器标签页上看到的标题。
admin.site.site_title = '后台管理系统'

#这两行代码可以放在任意一个admin.py里
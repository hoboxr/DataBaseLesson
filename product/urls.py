from django.urls import path
from .views import show_product, show_order, get_order, search_orders, cancel_order, search_categories, \
    order_area_charts, carrier_charts

app_name = 'product'
urlpatterns = [
    path('product/', show_product, name='show_product'),
    path('order/', show_order, name='show_order'),
    path('get_order/<slug:product_id>/', get_order, name='get_order'),
    path('search_orders/', search_orders, name='search_orders'),
    path('cancel_order/<slug:order_id>/', cancel_order, name='cancel_order'),
    path('search_categories/', search_categories, name='search_categories'),
    path('order_charts/', order_area_charts, name='order_charts'),
    path('carrier_charts', carrier_charts, name='carrier_charts'),
]

from django.shortcuts import render
from .models import Supplier, Category



def show_category(request):
    template_name = 'product/product_list.html'
    context = {
        'supplier_with_category_list': Supplier.objects.all(),
        'category_list': Category.objects.all()
    }
    return render(request, template_name, context)

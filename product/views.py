import random
from pyecharts import options as opts
from django.db.models import Count, IntegerField, When, Case
from pyecharts.charts import Bar, Pie, Line
from .models import Product, Order, OrderDetail
from customer.models import Customer
from supplier.models import Category
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime


def show_product(request):
    template_name = 'product/product_list.html'
    context = {
        'category_with_product_list': Category.objects.all(),
        'product_list': Product.objects.all(),
    }

    return render(request, template_name, context)


def show_order(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    user_id = request.session['user_id']

    OrderAll = Order.objects.filter(order_customer_id=user_id)
    total_price = 0
    total_charge = 0
    template_name = 'product/my_order.html'

    for item in OrderAll:
        total_price += item.product.product_price

    basic1_charge = 5
    basic2_charge = 10
    basic_else_charge = 3

    for item in OrderAll:
        orderDetail = OrderDetail.objects.filter(od_id=item.order_id).first()
        if item.product.category.category_id == '1':  # 谷物(长期）
            total_charge += int(basic1_charge + 0.25 * (pow(orderDetail.od_weight - 5, 2)))
        elif item.product.category.category_id == '2':  # 水产(短期)
            total_charge += int(basic2_charge + 0.5 * (pow(orderDetail.od_weight - 5, 2)))
        else:  # 其他(期限中等)
            total_charge += int(basic_else_charge + 0.3 * (pow(orderDetail.od_weight - 5, 2)))

    context = {
        'order_list': OrderAll,
        'total_price': total_price,
        'total_charge': total_charge,
    }
    return render(request, template_name, context)


def get_order(request, product_id):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    product = get_object_or_404(Product, product_id=product_id)
    user_id = request.session['user_id']

    try:
        user = Customer.objects.filter(customer_id=user_id).first()
        if user.address is None:
            messages.warning(request, "你还未填写地址信息哦~")
            return redirect('product:show_order')
        order = Order.objects.create(
            order_customer_id=user,
            order_C_name=user.customer_name,
            order_C_Address=user.address.customer_address,
            order_C_City=user.address.customer_city,
            order_C_Area=user.address.customer_area,
            order_C_PostalCode=user.address.customer_postalcode,
            order_C_Country=user.address.customer_country,
            order_orderdate=datetime.now(),
            product=product,
        )
        order.order_price = order.product.product_price
        product.product_inventory -= 1
        product.save()
        order.save()

        weight = random.randint(1, 5)
        quantity = 1
        notes = "无备注"
        orderDetail = OrderDetail.objects.create(
            od_id=order,
            od_product_id=product,
            od_weight=weight,
            od_quantity=quantity,
            od_notes=notes,
        )

        orderDetail.save()
        messages.success(request, '下单成功，请支付 {} 元'.format(order.order_price))
        return redirect("product:show_order")

    except ObjectDoesNotExist:
        messages.warning(request, "你还没有订单喵~")
        return redirect("product:show_order")


def search_orders(request):
    order_id = request.GET.get('order_id', '')
    try:
        order = Order.objects.get(order_id=order_id)
        return render(request, 'product/order_detail.html', {'order': order})
    except Order.DoesNotExist:
        messages.warning(request, "订单不存在喵~")
        return redirect("product:show_order")


def cancel_order(request, order_id):
    item = Order.objects.filter(order_id=order_id).first()
    if item is not None:
        item.delete()
    return redirect('product:show_order')


def search_categories(request):
    category_name = request.GET.get('category_name', '')
    if category_name:
        category = Category.objects.filter(category_name__icontains=category_name)
    else:
        category = Category.objects.all()
    context = {
        'category_with_product_list': category,
        'product_list': Product.objects.all(),
    }
    return render(request, 'product/product_list.html', context)


def order_area_charts(request):
    objs_hb = Order.objects.filter(order_C_Area="0")
    objs_db = Order.objects.filter(order_C_Area="1")
    objs_hd = Order.objects.filter(order_C_Area="2")
    objs_hx = Order.objects.filter(order_C_Area="3")
    objs_hz = Order.objects.filter(order_C_Area="4")
    objs_hn = Order.objects.filter(order_C_Area="5")
    objs_xn = Order.objects.filter(order_C_Area="6")
    objs_xb = Order.objects.filter(order_C_Area="7")
    order_area = ["华北", "东北", "华东", "华西", "华中", "华南", "西南", "西北"]
    order_data = [objs_hb.count(), objs_db.count(), objs_hd.count(), objs_hx.count(), objs_hz.count(),
                  objs_hn.count(),
                  objs_xn.count(), objs_xb.count()]
    pie_type = Pie()
    pie_type.add(
        "",
        [list(z) for z in zip(order_area, order_data)],
        center=["35%", "50%"],
    )
    pie_type = pie_type.render_embed()
    bar_type = Bar()
    bar_type.add_xaxis(order_area)
    bar_type.add_yaxis("订单数", order_data)
    bar_type = bar_type.render_embed()
    context = {'pie_type': pie_type, 'bar_type': bar_type}

    return render(request, 'product/order_area.html', context)


def carrier_charts(request):
    season_data = Order.objects.annotate(season=Case(
        When(order_senddate__month__in=[3, 4, 5], then=1),
        When(order_senddate__month__in=[6, 7, 8], then=2),
        When(order_senddate__month__in=[9, 10, 11], then=3),
        When(order_senddate__month__in=[12, 1, 2], then=4),
        output_field=IntegerField()
    )).values('season').annotate(count=Count('order_id')).order_by('season')
    season_bar = (
        Bar()
        .add_xaxis(['春季', '夏季', '秋季', '冬季'])
        .add_yaxis('订单量', [season['count'] for season in season_data])
        .set_global_opts(title_opts=opts.TitleOpts(title='不同季节的运货量统计'))
    )
    objs_hb = Order.objects.filter(order_C_Area="0")
    objs_db = Order.objects.filter(order_C_Area="1")
    objs_hd = Order.objects.filter(order_C_Area="2")
    objs_hx = Order.objects.filter(order_C_Area="3")
    objs_hz = Order.objects.filter(order_C_Area="4")
    objs_hn = Order.objects.filter(order_C_Area="5")
    objs_xn = Order.objects.filter(order_C_Area="6")
    objs_xb = Order.objects.filter(order_C_Area="7")
    order_area = ["华北", "东北", "华东", "华西", "华中", "华南", "西南", "西北"]
    order_data = [objs_hb.count(), objs_db.count(), objs_hd.count(), objs_hx.count(), objs_hz.count(),
                  objs_hn.count(),
                  objs_xn.count(), objs_xb.count()]
    line_type = Line()
    line_type.add_xaxis(order_area)
    line_type.add_yaxis("订单量", order_data, is_smooth=True)
    line_type.set_global_opts(title_opts=opts.TitleOpts(title="不同地区运货量统计"))
    context = {
        'line_type': line_type.render_embed(),
        'season_chart': season_bar.render_embed(),
    }
    return render(request, 'product/order_season.html', context)

from django.db import models
from supplier.models import Category, Supplier
from carrier.models import Carrier
from customer.models import Customer
from django.urls import reverse


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, verbose_name='产品ID')
    category = models.ForeignKey(Category, models.CASCADE, null=True, verbose_name='类别ID')
    product_name = models.CharField(max_length=255, verbose_name='产品名称', null=True)
    product_quantity = models.CharField(max_length=255, verbose_name='单位数量', null=True)
    product_price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='单价', null=True)
    product_photo = models.ImageField(upload_to='images/product', null=True, verbose_name='商品照片')
    product_inventory = models.SmallIntegerField(verbose_name='库存量', null=True)
    product_orderquantity = models.SmallIntegerField(verbose_name='订购量', null=True)
    product_reorderquanatity = models.SmallIntegerField(verbose_name='再订购量', null=True)
    product_status = models.IntegerField(choices=[(0, '中止'), (1, '在售')], verbose_name="状态", null=True)
    product_detail = models.TextField(null=True, verbose_name='商品描述')

    class Meta:
        ordering = ['product_id']
        db_table = 'product'
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product_name

    def get_order_url(self):
        return reverse("product:get_order", kwargs={'product_id': self.product_id})


class Information(models.Model):
    info_productbarch_id = models.IntegerField(verbose_name='产品批次ID', null=True)
    info_product = models.ForeignKey(Product, models.CASCADE, verbose_name='产品ID', null=True)
    info_productiondate = models.DateTimeField(verbose_name='生产日期', null=True)
    info_expirationdate = models.DateTimeField(verbose_name='保质期', null=True)

    class Meta:
        unique_together = ('info_productbarch_id', 'info_product')
        db_table = 'Information'
        verbose_name = "生产信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.info_productbarch_id)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='订单ID')
    order_customer_id = models.ForeignKey(Customer, models.CASCADE, null=True, verbose_name='客户ID')
    order_carrier_id = models.ForeignKey(Carrier, models.CASCADE, null=True, verbose_name='运货商ID')
    order_orderdate = models.DateTimeField(verbose_name='订购日期', null=True)
    order_senddate = models.DateTimeField(verbose_name='发货日期', null=True, blank=True)
    order_receivedate = models.DateTimeField(verbose_name='到货日期', null=True, blank=True)
    order_confirmdate = models.DateTimeField(verbose_name='货款确认日期', null=True, blank=True)
    order_price = models.CharField(max_length=255, verbose_name='订单价格', null=True)
    order_charge = models.CharField(max_length=255, verbose_name='运费', null=True, blank=True)
    order_C_name = models.CharField(max_length=255, verbose_name='货主名称', null=True)
    order_C_Address = models.CharField(max_length=255, verbose_name='货主地址', null=True)
    order_C_City = models.CharField(max_length=255, verbose_name='货主城市', null=True)
    order_C_Area = models.IntegerField(
        choices=[(0, '华北'), (1, '东北'), (2, '华东'), (3, '华西'), (4, '华中'), (5, '华南'), (6, '西南'), (7, '西北')],
        verbose_name="地区", default=1, null=True)
    order_C_PostalCode = models.CharField(max_length=255, verbose_name='货主邮政编码', null=True)
    order_C_Country = models.CharField(max_length=255, verbose_name='货主国家', null=True)
    order_Payway = models.CharField(max_length=255, verbose_name='支付方式', null=True, blank=True)
    order_Insurance = models.IntegerField(choices=[(0, '不使用保险'), (1, '使用保险')], verbose_name="保险信息", default=1,
                                          null=True)
    product = models.ForeignKey(Product, models.SET_NULL, null=True, verbose_name='产品ID')

    class Meta:
        ordering = ['order_id']
        db_table = 'Order'
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_id)


class OrderDetail(models.Model):
    od_id = models.ForeignKey(Order, models.CASCADE, null=True, verbose_name='订单ID')
    od_product_id = models.ForeignKey(Product, models.CASCADE, null=True, verbose_name='产品ID')
    od_weight = models.SmallIntegerField(verbose_name='重量', null=True)
    od_quantity = models.SmallIntegerField(verbose_name='数量', null=True)
    od_notes = models.TextField(verbose_name='备注', null=True)

    class Meta:
        ordering = ['od_id']
        db_table = 'OrderDetail'
        verbose_name = "订单明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.od_id)

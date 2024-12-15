from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name='客户ID')
    customer_name = models.CharField(max_length=255, verbose_name='联系人姓名', null=True)
    customer_password = models.CharField(max_length=255, verbose_name='客户密码', null=True)
    customer_tel = models.CharField(max_length=255, verbose_name="客户电话", null=True)
    address = models.ForeignKey('Address', models.SET_NULL, null=True, blank=True, verbose_name='地址')
    customer_status = models.IntegerField(choices=[(0, '离线'), (1, '在线')], default=0, verbose_name="客户状态")

    class Meta:
        ordering = ['customer_id']
        db_table = 'Customer'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.customer_name


class Address(models.Model):
    address_id = models.AutoField(primary_key=True, verbose_name="地址ID")
    customer_address = models.CharField(max_length=255, verbose_name="联系人地址", null=True)
    customer_company = models.CharField(max_length=255, verbose_name="公司名称", null=True)
    customer_job = models.CharField(max_length=255, verbose_name="联系人职业", null=True)
    customer_city = models.CharField(max_length=255, verbose_name="城市", null=True)
    customer_area = models.IntegerField(
        choices=[(0, '华北'), (1, '东北'), (2, '华东'), (3, '华西'), (4, '华中'), (5, '华南'), (6, '西南'), (7, '西北')],
        verbose_name="地区", default=1, null=True)
    customer_postalcode = models.CharField(max_length=255, verbose_name="邮政编码", null=True)
    customer_fax = models.CharField(max_length=255, verbose_name="传真", null=True)
    customer_country = models.CharField(max_length=255, verbose_name="国家", null=True)

    class Meta:
        ordering = ['address_id']
        db_table = 'Address'
        verbose_name = "地址信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.customer_address

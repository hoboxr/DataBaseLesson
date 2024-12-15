from django.db import models


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True, verbose_name='供应商ID')
    supplier_company = models.CharField(max_length=255, verbose_name='公司名称', null=True)
    supplier_name = models.CharField(max_length=255, verbose_name='联系人姓名', null=True)
    supplier_job = models.CharField(max_length=255, verbose_name='联系人职务', null=True)
    supplier_address = models.CharField(max_length=255, verbose_name='地址', null=True)
    supplier_city = models.CharField(max_length=255, verbose_name='城市', null=True)
    supplier_area = models.CharField(max_length=255, verbose_name='地区', null=True)
    supplier_postalcode = models.CharField(max_length=255, verbose_name='邮政编码', null=True)
    supplier_country = models.CharField(max_length=255, verbose_name='国家', null=True)
    supplier_tel = models.CharField(max_length=255, verbose_name='电话', null=True)
    supplier_fax = models.CharField(max_length=255, verbose_name='传真', null=True,blank=True)
    supplier_homepage = models.ImageField(upload_to='images/supplier', verbose_name='主页照片', null=True,blank=True)
    supplier_status = models.IntegerField(choices=[(0, '歇业中'), (1, '营业中')], verbose_name="状态", null=True)

    class Meta:
        ordering = ['supplier_id']
        db_table = 'Supplier'
        verbose_name = "供应商信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.supplier_company


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, verbose_name='类别ID')
    category_name = models.CharField(max_length=255, verbose_name='类别名称', null=True)
    category_notes = models.TextField(verbose_name='类别说明', null=True)
    category_photo = models.ImageField(upload_to='images/category', null=True,blank=True, verbose_name='图片')
    category_inittime = models.DateTimeField(verbose_name='创建时间', null=True)
    category_updatetime = models.DateTimeField(verbose_name='更新时间', null=True,blank=True)
    supplier = models.ForeignKey(Supplier, models.CASCADE, verbose_name='供应商', null=True)

    class Meta:
        ordering = ['category_id']
        db_table = 'Category'

        verbose_name = "商品类别信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.category_id)

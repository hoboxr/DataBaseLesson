from django.db import models

# Create your models here.
from django.db import models


class Carrier(models.Model):
    carrier_id = models.AutoField(primary_key=True, verbose_name='运货商ID')
    carrier_company = models.CharField(max_length=80, verbose_name='公司名称', null=True)
    carrier_vehicle = models.CharField(max_length=10, verbose_name='运输工具', null=True)
    carrier_tel = models.CharField(max_length=48, verbose_name="电话", null=True)
    carrier_status = models.IntegerField(choices=[(0, '不可使用'), (1, '可使用')], verbose_name="状态", null=True)

    class Meta:
        ordering = ['carrier_id']
        db_table = 'Carrier'
        verbose_name = "运货商信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.carrier_company

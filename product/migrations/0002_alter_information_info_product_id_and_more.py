# Generated by Django 5.0.4 on 2024-04-23 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="info_product_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
                verbose_name="产品ID",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_C_Address",
            field=models.CharField(max_length=255, null=True, verbose_name="货主地址"),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_C_City",
            field=models.CharField(max_length=255, null=True, verbose_name="货主城市"),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_C_Country",
            field=models.CharField(max_length=255, null=True, verbose_name="货主国家"),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_C_PostalCode",
            field=models.CharField(max_length=255, null=True, verbose_name="货主邮政编码"),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_C_name",
            field=models.CharField(max_length=255, null=True, verbose_name="货主名称"),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_Payway",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="支付方式"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(max_length=255, null=True, verbose_name="产品名称"),
        ),
        migrations.AlterField(
            model_name="product",
            name="product_quantity",
            field=models.CharField(max_length=255, null=True, verbose_name="单位数量"),
        ),
    ]

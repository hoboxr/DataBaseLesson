# Generated by Django 5.0.4 on 2024-04-23 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_alter_order_order_charge_alter_order_order_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="info_product_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
                verbose_name="产品ID",
            ),
        ),
        migrations.AlterField(
            model_name="information",
            name="info_productbarch_id",
            field=models.IntegerField(null=True, verbose_name="产品批次ID"),
        ),
    ]

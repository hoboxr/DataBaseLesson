# Generated by Django 5.0.4 on 2024-04-23 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_alter_information_info_product_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="information",
            old_name="info_product_id",
            new_name="info_product",
        ),
        migrations.AlterUniqueTogether(
            name="information",
            unique_together={("info_productbarch_id", "info_product")},
        ),
    ]

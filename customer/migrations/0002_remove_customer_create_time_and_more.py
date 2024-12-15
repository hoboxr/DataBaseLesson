# Generated by Django 5.0.4 on 2024-04-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="create_time",
        ),
        migrations.AlterField(
            model_name="address",
            name="customer_address",
            field=models.CharField(max_length=255, null=True, verbose_name="联系人地址"),
        ),
        migrations.AlterField(
            model_name="address",
            name="customer_city",
            field=models.CharField(max_length=255, null=True, verbose_name="城市"),
        ),
        migrations.AlterField(
            model_name="address",
            name="customer_company",
            field=models.CharField(max_length=255, null=True, verbose_name="公司名称"),
        ),
        migrations.AlterField(
            model_name="address",
            name="customer_country",
            field=models.CharField(max_length=255, null=True, verbose_name="国家"),
        ),
        migrations.AlterField(
            model_name="address",
            name="customer_fax",
            field=models.CharField(max_length=255, null=True, verbose_name="传真"),
        ),
        migrations.AlterField(
            model_name="address",
            name="customer_job",
            field=models.CharField(max_length=255, null=True, verbose_name="联系人职业"),
        ),
        migrations.AlterField(
            model_name="address",
            name="customer_postalcode",
            field=models.CharField(max_length=255, null=True, verbose_name="邮政编码"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_name",
            field=models.CharField(max_length=255, null=True, verbose_name="联系人姓名"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_password",
            field=models.CharField(max_length=255, null=True, verbose_name="客户密码"),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_tel",
            field=models.CharField(max_length=255, null=True, verbose_name="客户电话"),
        ),
    ]

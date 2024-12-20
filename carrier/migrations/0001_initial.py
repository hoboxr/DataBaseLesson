# Generated by Django 4.2.11 on 2024-04-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('carrier_id', models.AutoField(primary_key=True, serialize=False, verbose_name='运货商ID')),
                ('carrier_company', models.CharField(max_length=80, null=True, verbose_name='公司名称')),
                ('carrier_vehicle', models.CharField(max_length=10, null=True, verbose_name='运输工具')),
                ('carrier_tel', models.CharField(max_length=48, null=True, verbose_name='电话')),
                ('carrier_status', models.IntegerField(choices=[(0, '不可使用'), (1, '可使用')], null=True, verbose_name='状态')),
            ],
            options={
                'verbose_name': '运货商信息',
                'verbose_name_plural': '运货商信息',
                'db_table': 'Carrier',
                'ordering': ['carrier_id'],
            },
        ),
    ]

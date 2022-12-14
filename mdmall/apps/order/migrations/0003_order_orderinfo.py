# Generated by Django 3.2 on 2022-05-24 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_ordertemp_specification'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(blank=True, null=True, verbose_name='商品id')),
                ('goods_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='商品名称')),
                ('goods_img', models.CharField(blank=True, max_length=500, null=True, verbose_name='图片路径')),
                ('goods_count', models.IntegerField(blank=True, null=True, verbose_name='商品数量')),
                ('goods_price', models.FloatField(blank=True, null=True, verbose_name='商品价格')),
                ('total_price', models.FloatField(blank=True, null=True, verbose_name='商品总价格')),
                ('goods_status', models.CharField(blank=True, max_length=200, null=True, verbose_name='商品状态码')),
                ('category_id', models.IntegerField(blank=True, null=True, verbose_name='商品类别')),
                ('specification', models.CharField(blank=True, max_length=200, null=True, verbose_name='商品规格')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='关联用户')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'md_order_info',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='订单id')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='订单创建事件')),
                ('order_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='订单名称')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='关联用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'md_order',
            },
        ),
    ]

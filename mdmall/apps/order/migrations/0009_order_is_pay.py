# Generated by Django 3.2 on 2022-05-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_price_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_pay',
            field=models.BooleanField(default=False, verbose_name='是否支付'),
        ),
    ]
# Generated by Django 3.2 on 2022-05-25 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_remove_order_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order', verbose_name='关联订单'),
        ),
    ]

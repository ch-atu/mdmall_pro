# Generated by Django 3.2 on 2022-05-19 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20220519_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilegoods',
            name='estimate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.estimate', verbose_name='商品评价'),
        ),
    ]
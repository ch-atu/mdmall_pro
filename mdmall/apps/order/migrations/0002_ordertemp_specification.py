# Generated by Django 3.2 on 2022-05-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertemp',
            name='specification',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='商品规格'),
        ),
    ]

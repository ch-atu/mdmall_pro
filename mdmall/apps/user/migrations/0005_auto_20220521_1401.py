# Generated by Django 3.2 on 2022-05-21 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.utils


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': '用户名只能是唯一的'}, max_length=150, unique=True, validators=[user.utils.validate_username], verbose_name='用户名'),
        ),
        migrations.CreateModel(
            name='UserHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(blank=True, max_length=200, null=True, verbose_name='所在地区')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
                'db_table': 'user_home',
            },
        ),
    ]

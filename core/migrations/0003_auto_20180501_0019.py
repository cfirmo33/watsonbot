# Generated by Django 2.0 on 2018-05-01 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180427_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastusercontext',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.UserTelegram', unique=True),
        ),
    ]

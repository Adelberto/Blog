# Generated by Django 2.0.5 on 2018-06-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20180603_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(verbose_name='03 Jun, 2018 - 17h15m'),
        ),
    ]

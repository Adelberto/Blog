# Generated by Django 2.0.5 on 2018-06-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180603_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(verbose_name='03, Jun 2018 - 17H02m'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to=''),
        ),
    ]

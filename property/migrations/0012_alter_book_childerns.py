# Generated by Django 3.2 on 2023-08-03 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20230802_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='childerns',
            field=models.IntegerField(blank=True, choices=[(4, 4), (5, 5), (3, 3), (2, 2), (1, 1)], null=True, verbose_name='childerns'),
        ),
    ]

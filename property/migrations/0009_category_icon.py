# Generated by Django 3.2 on 2023-07-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_property_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='', max_length=50, verbose_name='icon'),
            preserve_default=False,
        ),
    ]

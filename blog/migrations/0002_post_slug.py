# Generated by Django 3.2 on 2023-07-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='slug'),
        ),
    ]

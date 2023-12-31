# Generated by Django 3.2 on 2023-08-08 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0002_auto_20230807_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about/images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='about',
            name='our_goal',
            field=models.TextField(verbose_name='our goal'),
        ),
        migrations.AlterField(
            model_name='about',
            name='what_we_do',
            field=models.TextField(verbose_name='what we do?'),
        ),
        migrations.AlterField(
            model_name='about',
            name='who_we_are',
            field=models.TextField(verbose_name='who we are?'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=500, verbose_name='question'),
        ),
        migrations.AlterField(
            model_name='subscribtion',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='subscribtion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]

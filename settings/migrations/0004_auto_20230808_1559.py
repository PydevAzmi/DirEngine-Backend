# Generated by Django 3.2 on 2023-08-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20230807_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='company',
            name='call_us',
            field=models.CharField(max_length=25, verbose_name='Call_Us'),
        ),
        migrations.AlterField(
            model_name='company',
            name='desc',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='company',
            name='fb_link',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='company',
            name='insta_link',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='company',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='company/logo', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='twit_link',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter'),
        ),
    ]

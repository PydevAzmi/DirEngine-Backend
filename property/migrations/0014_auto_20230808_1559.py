# Generated by Django 3.2 on 2023-08-08 12:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0013_auto_20230807_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='childerns',
            field=models.IntegerField(blank=True, choices=[(4, 4), (5, 5), (3, 3), (2, 2), (1, 1)], null=True, verbose_name='childerns'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_from',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='booked from'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_to',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='booked to'),
        ),
        migrations.AlterField(
            model_name='book',
            name='guests',
            field=models.IntegerField(choices=[(4, 4), (5, 5), (3, 3), (2, 2), (1, 1)], verbose_name='guests'),
        ),
        migrations.AlterField(
            model_name='book',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_booked', to='property.property', verbose_name='property'),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=50, verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to='place/images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='avilablity',
            field=models.BooleanField(blank=True, null=True, verbose_name='avilabilty'),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_category', to='property.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='property',
            name='descritpion',
            field=models.TextField(verbose_name='descritpion'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(upload_to='property/images', verbose_name='main_image'),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='property_owner'),
        ),
        migrations.AlterField(
            model_name='property',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_places', to='property.place', verbose_name='places'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(default=0, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ImageField(upload_to='property/images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='propertyimages',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_images', to='property.property', verbose_name='property'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=150, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='review',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_Reviews', to='property.property', verbose_name='property'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)], verbose_name='rate'),
        ),
    ]

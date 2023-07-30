# Generated by Django 3.2 on 2023-07-30 08:52

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(upload_to=accounts.models.user_dir_path, verbose_name='profile_image')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, verbose_name='Gender')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
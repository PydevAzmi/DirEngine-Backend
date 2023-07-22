# Generated by Django 3.2 on 2023-07-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('who_we_are', models.TextField(verbose_name='who we are?')),
                ('what_we_do', models.TextField(verbose_name='what we do?')),
                ('our_goal', models.TextField(verbose_name='our goal')),
                ('image', models.ImageField(upload_to='about/images', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='question')),
                ('answer', models.TextField(verbose_name='answer')),
            ],
        ),
    ]

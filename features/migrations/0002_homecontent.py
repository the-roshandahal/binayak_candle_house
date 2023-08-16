# Generated by Django 4.1.4 on 2023-08-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=200)),
                ('header_heading', models.CharField(max_length=150)),
                ('header_text', models.TextField()),
                ('header_image', models.ImageField(upload_to='home_images/', verbose_name='Hero Section Image (1920*800)')),
                ('header_button_text', models.CharField(max_length=100)),
                ('header_button_url', models.URLField()),
                ('about_title', models.CharField(max_length=255)),
                ('about_text', models.TextField()),
                ('about_image', models.ImageField(upload_to='home_images/', verbose_name='About Image (500*600)')),
            ],
            options={
                'verbose_name_plural': '02.Home Page Content',
            },
        ),
    ]

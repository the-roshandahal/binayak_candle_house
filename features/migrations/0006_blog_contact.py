# Generated by Django 4.1.4 on 2023-08-16 07:31

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_gallery_alter_product_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('blog', models.TextField()),
                ('image', models.ImageField(upload_to='blogs_images/', verbose_name='Blog Image (370*270)')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '06. Blogs',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('contact', models.TextField()),
                ('subject', models.TextField(blank=True, null=True)),
                ('message', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '05. Contact',
            },
        ),
    ]

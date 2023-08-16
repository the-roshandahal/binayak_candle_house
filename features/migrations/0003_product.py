# Generated by Django 4.1.4 on 2023-08-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_homecontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', models.ImageField(upload_to='products_images/', verbose_name='Featured Image Image (200*200)')),
                ('product_title', models.CharField(max_length=255)),
                ('product_description', models.TextField()),
            ],
            options={
                'verbose_name_plural': '04. Products',
            },
        ),
    ]

# Generated by Django 4.1.4 on 2023-08-16 07:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

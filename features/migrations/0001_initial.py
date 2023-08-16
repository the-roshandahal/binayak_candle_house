# Generated by Django 4.1.4 on 2023-08-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_set', models.CharField(max_length=200)),
                ('company_logo', models.ImageField(upload_to='logos', verbose_name='Company Logo (163*36)')),
                ('company_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('opening_hours', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '01. Company Setup',
            },
        ),
    ]
# Generated by Django 4.1.4 on 2023-08-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0008_aboutpagecontent_fet_video_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagecontent',
            name='out_story',
            field=models.TextField(default='sdasdsa'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.9 on 2024-10-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_total_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='field1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='image',
            name='field2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
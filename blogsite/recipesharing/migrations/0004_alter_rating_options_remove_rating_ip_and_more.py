# Generated by Django 5.1.1 on 2024-09-16 03:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesharing', '0003_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='recipe',
        ),
        migrations.AddIndex(
            model_name='rating',
            index=models.Index(fields=['created'], name='recipeshari_created_20ecbd_idx'),
        ),
    ]

# Generated by Django 5.0.9 on 2024-12-06 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_portfolio'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='instructors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='portfolios_viewed', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='portfolios_created', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.9 on 2024-12-08 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0006_portfoliocontent_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliocontent',
            name='owner',
        ),
    ]

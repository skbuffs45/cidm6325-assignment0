# Generated by Django 5.0.9 on 2024-12-08 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('portfolios', '0004_alter_portfolio_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliocontent',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ('portfoliotext', 'portfoliovideo', 'portfolioimage', 'portfoliofile')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]

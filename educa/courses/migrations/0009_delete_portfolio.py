# Generated by Django 5.0.9 on 2024-12-07 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_remove_portfolio_instructors_portfolio_instructors'),
        ('students', '0003_remove_portfoliofile_owner_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]

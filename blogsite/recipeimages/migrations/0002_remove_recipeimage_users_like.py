# Generated by Django 5.0.9 on 2024-10-16 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeimages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeimage',
            name='users_like',
        ),
    ]

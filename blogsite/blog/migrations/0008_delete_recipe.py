# Generated by Django 5.0.9 on 2024-10-10 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_recipe_delete_recipes_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]

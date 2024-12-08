# Generated by Django 5.0.9 on 2024-12-07 19:19

import portfolios.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0003_portfoliocontent_portfoliofile_portfolioimage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='portfoliocontent',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='portfolio',
            name='order',
            field=portfolios.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfoliocontent',
            name='order',
            field=portfolios.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
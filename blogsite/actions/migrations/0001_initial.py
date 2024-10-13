# Generated by Django 5.0.9 on 2024-10-13 19:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('target_id', models.PositiveIntegerField(blank=True, null=True)),
                ('target_ct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_obj', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='actions_act_created_64f10d_idx'), models.Index(fields=['target_ct', 'target_id'], name='actions_act_target__f20513_idx')],
            },
        ),
    ]

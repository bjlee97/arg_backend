# Generated by Django 2.1 on 2021-10-20 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arg_backend', '0002_teams_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='generic',
        ),
    ]
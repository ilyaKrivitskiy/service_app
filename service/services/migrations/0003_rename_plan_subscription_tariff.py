# Generated by Django 3.2.25 on 2024-09-13 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20240911_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='plan',
            new_name='tariff',
        ),
    ]

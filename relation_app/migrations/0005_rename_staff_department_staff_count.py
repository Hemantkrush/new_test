# Generated by Django 4.1 on 2022-11-04 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relation_app', '0004_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='staff',
            new_name='staff_count',
        ),
    ]

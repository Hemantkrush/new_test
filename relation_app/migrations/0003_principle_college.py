# Generated by Django 4.1 on 2022-11-04 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation_app', '0002_alter_college_table_alter_principle_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='principle',
            name='college',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='relation_app.college'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1 on 2022-11-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relation_app', '0007_college_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relation_app.college'),
        ),
    ]

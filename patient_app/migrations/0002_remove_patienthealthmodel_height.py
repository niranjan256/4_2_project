# Generated by Django 4.2 on 2024-03-15 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patienthealthmodel',
            name='height',
        ),
    ]
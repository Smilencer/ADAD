# Generated by Django 2.2.1 on 2019-06-03 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0008_symptom_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_info',
            name='age',
        ),
    ]

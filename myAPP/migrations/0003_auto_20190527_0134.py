# Generated by Django 2.2.1 on 2019-05-26 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0002_auto_20190525_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_info',
            old_name='userID',
            new_name='user',
        ),
    ]

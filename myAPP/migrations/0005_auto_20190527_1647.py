# Generated by Django 2.2.1 on 2019-05-27 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0004_auto_20190527_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='myAPP.login_info', unique=True),
        ),
    ]

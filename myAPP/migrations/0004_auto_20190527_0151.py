# Generated by Django 2.2.1 on 2019-05-26 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0003_auto_20190527_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_info',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='myAPP.login_info'),
        ),
    ]

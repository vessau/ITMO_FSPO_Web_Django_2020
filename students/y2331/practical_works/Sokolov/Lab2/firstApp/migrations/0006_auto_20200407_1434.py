# Generated by Django 3.0.5 on 2020-04-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_auto_20200407_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverslicense',
            name='licenseNumber',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

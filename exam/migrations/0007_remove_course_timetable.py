# Generated by Django 3.0.5 on 2022-04-29 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Timetable',
        ),
    ]

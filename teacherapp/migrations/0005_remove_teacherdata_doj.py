# Generated by Django 2.2.23 on 2022-03-14 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0004_auto_20220314_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherdata',
            name='doj',
        ),
    ]

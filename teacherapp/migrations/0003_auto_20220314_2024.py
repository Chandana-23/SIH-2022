# Generated by Django 2.2.23 on 2022-03-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0002_teacherdata_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherdata',
            name='status',
            field=models.TextField(choices=[('active', 'Active'), ('long leave', 'Long Leave'), ('sick leave', 'Sick Leave'), ('metarnity', 'Metarnity Leave')], default='active'),
        ),
    ]
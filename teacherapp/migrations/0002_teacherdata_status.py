# Generated by Django 2.2.23 on 2022-03-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherdata',
            name='status',
            field=models.TextField(default='active', verbose_name=(('active', 'Active'), ('long leave', 'Long Leave'), ('sick leave', 'Sick Leave'), ('metarnity', 'Metarnity Leave'))),
        ),
    ]

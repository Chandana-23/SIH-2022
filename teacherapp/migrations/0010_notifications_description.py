# Generated by Django 4.0 on 2022-03-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0009_delete_personaldata_delete_teacherdata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 4.0 on 2022-03-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0013_remove_members_user_id_alter_members_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('job_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('job_name', models.TextField()),
            ],
        ),
    ]

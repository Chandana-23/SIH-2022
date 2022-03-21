# Generated by Django 2.2.23 on 2022-03-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('doj', models.DateField()),
                ('age', models.IntegerField()),
                ('qualification', models.TextField()),
                ('designation', models.TextField()),
            ],
        ),
    ]

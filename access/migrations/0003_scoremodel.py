# Generated by Django 2.2.6 on 2019-11-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_auto_20191113_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='scoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('number', models.IntegerField(max_length=250)),
                ('score', models.IntegerField(max_length=250)),
                ('assesment_time', models.CharField(max_length=250)),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-21 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('number', models.IntegerField()),
                ('score', models.TextField(max_length=25)),
                ('assesment_time', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='undecided', max_length=250)),
            ],
        ),
    ]

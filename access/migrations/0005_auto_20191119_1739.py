# Generated by Django 2.2.6 on 2019-11-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_auto_20191119_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowMoringa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(default='email@gmail.com', max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]

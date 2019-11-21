

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='interestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='Nan', max_length=250)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=250)),
                ('guardians_number', models.TextField(default='Nan', max_length=250)),
                ('age', models.TextField(max_length=250)),
                ('date_of_birth', models.CharField(max_length=250)),
                ('gender', models.TextField(max_length=250)),
                ('prior_acceptance', models.TextField(max_length=250)),
                ('highest_education_level', models.TextField(default='Nan', max_length=250)),
                ('bachelors_degree', models.CharField(default='Nan', max_length=250)),
                ('completion_date', models.CharField(max_length=250)),
                ('applied_to_uni', models.CharField(max_length=250)),
                ('start_date', models.CharField(max_length=250)),
                ('moringa_student', models.CharField(max_length=250)),
                ('class_name', models.CharField(max_length=250)),
                ('commitment', models.CharField(max_length=250)),
                ('refered_by', models.CharField(max_length=250)),
                ('computer_literacy', models.CharField(max_length=250)),
                ('fluency', models.CharField(max_length=250)),
                ('residence', models.CharField(max_length=250)),
                ('residence_other', models.CharField(max_length=250)),
                ('residence_clarification', models.CharField(max_length=250)),
            ],
        ),
    ]

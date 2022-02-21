# Generated by Django 2.2.3 on 2019-07-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myApp', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('std_number', models.IntegerField()),
                ('teacher', models.CharField(choices=[('ahmadi', 'Ahmadi'), ('adbi', 'Abdi'), ('bahrami', 'Bahrami')], max_length=7)),
            ],
        ),
    ]

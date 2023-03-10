# Generated by Django 4.1.7 on 2023-03-02 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_age', models.CharField(max_length=20)),
                ('s_gender', models.CharField(max_length=200)),
                ('s_email', models.CharField(max_length=100)),
                ('s_phone', models.CharField(max_length=200)),
                ('s_username', models.CharField(max_length=100)),
                ('s_password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'student_tb',
            },
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-21 07:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CONTACT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=300, null=True)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NOTICE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=50)),
                ('notice', models.FileField(blank=True, upload_to='resume')),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RESUME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('resume', models.FileField(upload_to='resume')),
            ],
        ),
    ]

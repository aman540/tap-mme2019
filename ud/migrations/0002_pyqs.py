# Generated by Django 4.0.4 on 2022-05-22 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PYQS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('company', models.CharField(max_length=200)),
                ('note', models.TextField(null=True)),
                ('question', models.FileField(blank=True, upload_to='pyqs')),
            ],
        ),
    ]

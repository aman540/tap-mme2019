# Generated by Django 4.0.4 on 2022-05-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ud', '0006_alter_pyqs_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyqs',
            name='question',
            field=models.FileField(blank=True, upload_to='pyqs'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.FileField(null=True, upload_to='image'),
        ),
    ]

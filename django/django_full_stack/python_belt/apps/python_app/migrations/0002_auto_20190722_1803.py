# Generated by Django 2.2.3 on 2019-07-22 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('python_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

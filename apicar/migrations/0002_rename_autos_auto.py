# Generated by Django 4.1.2 on 2022-10-07 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apicar', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autos',
            new_name='Auto',
        ),
    ]
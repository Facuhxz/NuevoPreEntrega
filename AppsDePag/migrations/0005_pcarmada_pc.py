# Generated by Django 5.0.6 on 2024-06-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppsDePag', '0004_rename_portatiles_portatilgamer'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcarmada',
            name='pc',
            field=models.CharField(default='', max_length=10),
        ),
    ]

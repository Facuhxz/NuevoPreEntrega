# Generated by Django 5.0.6 on 2024-06-18 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppsDePag', '0002_pcarmada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portatiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=25)),
                ('modelo', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='MotherBoard',
        ),
    ]
